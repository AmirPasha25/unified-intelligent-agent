from langchain_tavily import TavilySearch
from langchain.tools import Tool

class TavilySearchEnginer:
    def __init__(self, tavily_api_key):
          self.tavily_api_key = tavily_api_key
          
    def search_engine(self, query:str):
            search_engine_func = TavilySearch(tavily_api_key =  self.tavily_api_key, search_depth="basic")
            return search_engine_func.run(query)
    

searchengine = TavilySearchEnginer("please enter your tavily sereach engine key here plzz.")
tavily_search_tool = Tool(name = "SearchEngine",
                                  func=searchengine.search_engine,
                                  description= "NOTE: CALL THIS FUNCTION FOR ANY KIND OF REAL TIME DATA", verbose = True)