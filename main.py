# main.py
from langgraph.prebuilt import create_react_agent
from toolcalling import calltools
from llm import openai_llm   # you already created it in llm.py

class AgentB:
    def __init__(self):
        print("Hi Welcome to Super Intelligent AI Agent Designed by Amir Pasha")
        self.agent = create_react_agent(
            model=openai_llm.llm,
            tools=calltools
        )

    def run(self):
        user_input = input("Enter your query here: ")
        final_output = self.agent.invoke({"messages": [("user", user_input)]})
        if "output" in final_output:
            print("Agent Response:", final_output["output"])
        elif "messages" in final_output:
            ai_message = final_output["messages"][-1].content if final_output["messages"] else "No message returned"
            print("Agent Response", ai_message)
        else:
            print("Unexpected Output:", final_output)


AgentB().run()
