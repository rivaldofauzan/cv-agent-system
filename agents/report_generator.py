from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser

# Prompt template for the Report Generator Agent
REPORT_GENERATOR_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a senior career strategist and technical recruiter. Your task is to generate a comprehensive, well-structured report for a hiring manager.
You will synthesize the candidate's skill analysis and the current market demands for the target role.

The report must be in Markdown format and include the following sections:
1.  **Key Strengths Analysis:** A summary of the candidate's strongest and most relevant skills.
2.  **Current Market Demands:** A summary of what the market is looking for in the target role.
3.  **Skill-Gap Analysis:** A Markdown table comparing the candidate's skills against market demands, highlighting any gaps.
4.  **Personalized Upskilling Plan:** Actionable, specific recommendations for the candidate to bridge the gaps.

Ensure the tone is professional, insightful, and data-driven. The final output should be a single, complete Markdown document.
""",
        ),
        (
            "human",
            """Please generate the report based on the following information:
            
**Target Role:** {target_role}

**Candidate's Skill Analysis:**
```json
{skill_analysis}
```

**Market Demands Summary:**
```text
{market_demands}
```
""",
        ),
    ]
)

def generate_report(state: dict):
    """
    Node function for the Recommendation & Report Agent.
    
    This agent synthesizes the analysis from the skill analyst and market intelligence agents
    to generate a comprehensive report.

    Args:
        state (dict): The current state of the graph.

    Returns:
        dict: The updated state with the final_report field populated.
    """
    print("---GENERATING FINAL REPORT---")
    target_role = state["target_role"]
    skill_analysis = state["skill_analysis"]
    market_demands = state["market_demands"]
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.2)
    
    # Chain the prompt with the LLM and a string output parser
    chain = REPORT_GENERATOR_PROMPT | llm | StrOutputParser()
    
    final_report = chain.invoke({
        "target_role": target_role,
        "skill_analysis": skill_analysis,
        "market_demands": market_demands,
    })
    
    print("---REPORT GENERATED SUCCESSFULLY---")
    
    return {"final_report": final_report}

