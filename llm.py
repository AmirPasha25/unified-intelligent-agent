from langchain_openai import ChatOpenAI
from langchain.tools import Tool

class LLM:
    def __init__ (self, openaikey):
        self.openaikey = openaikey
        self.llm = ChatOpenAI(model="gpt-5-nano", 
                              temperature = 0.7, 
                              api_key = self.openaikey, # pyright: ignore[reportCallIssue]
                              )
        
    def llm_model(self, query:str):
        response = self.llm.invoke(query)
        return response.content

openai_llm = LLM("Please Enter your API key - only openai api keys are allowed")
openai_llm_tool = Tool(name = "LLMModel",
                       func=openai_llm.llm_model,
                       description= "NOTE: CALL THIS FUNCTION FOR ANY KIND OF REASONING. " \
                        "IF ALL OTHER FAILS TO DO THE WORK YOU HAVE TO HANDLE AND GIVE MOST CORRECT AND ACCURATE ANSWER",
                        verbose = True)


