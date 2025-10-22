from datetime import date
from datetime import datetime
from langchain.tools import Tool

class TimeDate:
    def currenttime(self, query:str):
        time = datetime.now()
        return time

    def ctim(self, query:str):
        today = date.today()
        ctim = today.ctime()
        return ctim
    
    def currentdate(self, query:str):
        today = date.today()
        return today
    
    def currentweek(self, query:str):
        today = date.today()
        weekday = today.weekday()
        return weekday
    
    def currentisoweek(self, query:str):
        today = date.today()
        month = today.isoweekday()
        return month

    def currentmonth(self, query:str):
        today = date.today()
        month = today.month
        return month
    
    
time_date = TimeDate()
current_time = Tool(name = "CurrentTime",
                 func=time_date.currenttime,
                 description= '''NOTE: FOR TODAY'S DATE AND FOR CURRENT TIME ALWAYS USE THIS FUNCTION''', verbose = True)
current_ctim = Tool(name = "Currentctime",
                 func=time_date.ctim,
                 description= '''NOTE: FOR TODAY'S DATE AND FOR CURRENT TIME ALWAYS USE THIS FUNCTION''', verbose = True)
current_date = Tool(name = "CurrentDate",
                 func=time_date.currentdate,
                 description= '''NOTE: FOR TODAY'S DATE AND FOR CURRENT TIME ALWAYS USE THIS FUNCTION''', verbose = True)
current_week = Tool(name = "CurrentWeek",
                 func=time_date.currentweek,
                 description= '''NOTE: FOR TODAY'S DATE AND FOR CURRENT TIME ALWAYS USE THIS FUNCTION''', verbose = True)
current_month = Tool(name = "CurrentMonth",
                 func=time_date.currentmonth,
                 description= '''NOTE: FOR TODAY'S DATE AND FOR CURRENT TIME ALWAYS USE THIS FUNCTION''', verbose = True)
