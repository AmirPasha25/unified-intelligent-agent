from clock import current_time, current_ctim, current_date, current_week, current_month
from mathematics import math_tool1, math_tool2, math_tool3
from llm import openai_llm_tool
from searchengine import tavily_search_tool
from weather import weather_tool

class CallTools:
    def __init__ (self):
        self.openaillm = openai_llm_tool
        self.searchengine = tavily_search_tool
        self.currenttime = current_time
        self.currentctim = current_ctim
        self.currentdate = current_date
        self.currentweek = current_week
        self.currentmonth = current_month
        self.mathematics1 = math_tool1
        self.mathematics2 = math_tool2
        self.mathematics3 = math_tool3
        self.weathertool = weather_tool
    
    def calling_tools(self):
        my_tools = [self.openaillm,
                    self.searchengine,
                    self.currenttime,
                    self.currentctim,
                    self.currentdate,
                    self.currentweek,
                    self.currentmonth,
                    self.mathematics1,
                    self.mathematics2,
                    self.mathematics3,
                    self.weathertool]
        
        return my_tools
calltools = CallTools().calling_tools()




        
