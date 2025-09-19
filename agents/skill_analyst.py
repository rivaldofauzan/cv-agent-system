from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Prompt template for the Skill Analyst Agent
SKILL_ANALYST_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a world-class Senior AI Engineer and a hiring manager.
Your task is to analyze the provided structured CV data to get a deep understanding of the candidate's capabilities.
You must identify both explicit skills (directly listed) and implicit skills (inferred from projects and experience).

For example, if a project mentions 'building a RAG system with LangChain', you should infer skills like 'Information Retrieval', 'Vector Databases', and 'LLM Application Development'.

Provide a justification for each implicit skill you identify.
Return the analysis as a JSON object with two keys: 'explicit_skills' and 'implicit_skills'.
'explicit_skills' should be a list of strings.
'implicit_skills' should be a list of objects, each with 'skill' and 'justification' keys.
Do not output anything other than the JSON object.
""",
        ),
        (
            "human",
            "Here is the structured CV data:\n\n```json\n{structured_cv}\n```",
        ),
    ]
)


def analyze_skills(state: dict):
    """
    Node function for the Specialized Skill Analyst Agent.
    
    This agent analyzes the structured CV to infer a deeper understanding
    of the candidate's capabilities, identifying both explicit and implicit skills.

    Args:
        state (dict): The current state of the graph.

    Returns:
        dict: The updated state with the skill_analysis field populated.
    """
    print("---ANALYZING SKILLS---")
    structured_cv = state["structured_cv"]
    
    # Initialize Gemini model with JSON response format
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash-latest", 
        temperature=0,
    )
    
    # Chain the prompt with the LLM and a JSON output parser
    parser = JsonOutputParser()
    chain = SKILL_ANALYST_PROMPT | llm | parser
    
    # Invoke the chain with the structured CV
    skill_analysis = chain.invoke({"structured_cv": structured_cv.dict()})
    
    print("---SKILLS ANALYZED SUCCESSFULLY---")
    
    return {"skill_analysis": skill_analysis}

