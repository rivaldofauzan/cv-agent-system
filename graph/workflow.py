from langgraph.graph import StateGraph, END
from .state import AgentState

# Import agent node functions
from agents.cv_parser import parse_cv
from agents.skill_analyst import analyze_skills
from agents.market_intel import research_market
from agents.report_generator import generate_report

def build_graph():
    """
    Builds the LangGraph workflow.

    This function defines the nodes and edges of our multi-agent system.
    The graph starts with CV parsing, then proceeds to parallel analysis of skills
    and market demands, and finally synthesizes the information into a report.

    Returns:
        Compiled LangGraph application.
    """
    workflow = StateGraph(AgentState)

    # 1. Add the nodes
    workflow.add_node("cv_parser", parse_cv)
    workflow.add_node("skill_analyst", analyze_skills)
    workflow.add_node("market_researcher", research_market)
    workflow.add_node("report_generator", generate_report)

    # 2. Define the edges (the flow of control)
    
    # The entry point is the cv_parser
    workflow.set_entry_point("cv_parser")
    
    # After parsing, run the skill analyst and market researcher in parallel
    workflow.add_edge("cv_parser", "skill_analyst")
    workflow.add_edge("cv_parser", "market_researcher")
    
    # After both parallel nodes are done, join them at the report generator
    workflow.add_node("join_node", lambda x: x)
    workflow.add_edge("skill_analyst", "join_node")
    workflow.add_edge("market_researcher", "join_node")
    
    # From the join point, move to the report generator
    workflow.add_edge("join_node", "report_generator")
    
    # The report generator is the final step
    workflow.add_edge("report_generator", END)

    # 3. Compile the graph into a runnable application
    app = workflow.compile()
    
    return app

