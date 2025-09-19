import os
from langchain_community.tools.tavily_search import TavilySearchResults

def get_search_tool():
    """
    Initializes and returns the Tavily search tool.
    
    The Tavily API key is fetched from environment variables.
    This tool is used by the Market Intelligence Agent to find
    real-time information about job market trends.
    """
    # Note: The TAVILY_API_KEY environment variable must be set.
    search_tool = TavilySearchResults(max_results=5)
    return search_tool

