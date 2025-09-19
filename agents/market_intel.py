from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent

from tools.search import get_search_tool

# Prompt template for the Market Intelligence Agent
MARKET_INTEL_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a market research analyst for a top-tier tech recruiting firm.
Your goal is to gather and summarize the most in-demand skills and technologies for a specific technical role.
You must use your search tool to query current job listings and industry trends from the last 6-12 months.

Synthesize your findings into a concise, easy-to-read summary. Focus on the top 10-15 most critical skills, frameworks, and concepts.
""",
        ),
        (
            "human",
            "Please research the current market demands for the role of: **{target_role}**",
        ),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

def research_market(state: dict):
    """
    Node function for the Market Intelligence Agent.
    
    This agent uses a search tool to query current job listings and industry trends
    for a specified technical role and summarizes the in-demand skills.

    Args:
        state (dict): The current state of the graph.

    Returns:
        dict: The updated state with the market_demands field populated.
    """
    print("---RESEARCHING MARKET DEMANDS---")
    target_role = state["target_role"]
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0)
    search_tool = get_search_tool()
    tools = [search_tool]
    
    # Create the agent using LangChain's create_tool_calling_agent
    agent = create_tool_calling_agent(llm, tools, MARKET_INTEL_PROMPT)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)
    
    # Invoke the agent executor
    response = agent_executor.invoke({
        "target_role": target_role,
    })
    
    market_demands = response['output']
    
    print("---MARKET RESEARCH COMPLETE---")
    
    return {"market_demands": market_demands}

