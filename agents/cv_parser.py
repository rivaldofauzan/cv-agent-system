from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticToolsParser


from graph.state import StructuredCV

# Prompt template for the CV parsing agent
CV_PARSER_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert data extraction agent.
Your task is to parse a raw CV text into a structured, machine-readable format using the provided `StructuredCV` tool.
You must adhere strictly to the provided JSON schema.
Ensure all relevant sections like experience, skills, education, and projects are accurately extracted.
If a section is missing from the CV, you can omit it from the output.""",
        ),
        (
            "human",
            "Please parse the following CV text:\n\n```text\n{cv_text}\n```",
        ),
    ]
)

def parse_cv(state: dict):
    """
    Node function for the CV Parsing Agent.
    
    This agent takes the raw CV text, uses a Gemini model with tool calling
    to extract structured data, and updates the state.

    Args:
        state (dict): The current state of the graph.

    Returns:
        dict: The updated state with the structured_cv field populated.
    """
    print("---PARSING CV---")
    cv_text = state["cv_text"]
    
    # Initialize the Gemini model
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0)
    
    # Bind the Pydantic model as a tool and create a parser
    llm_with_tools = llm.bind_tools([StructuredCV])
    parser = PydanticToolsParser(tools=[StructuredCV])

    # Chain the prompt with the LLM and parser
    chain = CV_PARSER_PROMPT | llm_with_tools | parser
    
    # Invoke the chain with the CV text
    # The result will be a list of Pydantic objects, we take the first one.
    structured_cv_list = chain.invoke({"cv_text": cv_text})

    # Add error handling to check if parsing was successful
    if not structured_cv_list:
        print("---ERROR: CV PARSING FAILED---")
        raise ValueError(
            "The CV parsing agent failed to extract any structured data. "
            "This could be due to an issue with the LLM or an empty CV."
        )
    
    print("---CV PARSED SUCCESSFULLY---")
    
    return {"structured_cv": structured_cv_list[0]}

