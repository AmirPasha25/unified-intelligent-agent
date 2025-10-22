import sympy
import numpy
import scipy
from langchain.tools import Tool

class Mathematics:
    def mathematics1(self, query: str):
        try:
            functions_list = {i: getattr(sympy, i) for i in dir(sympy)}
            final_sympy_functions = {"__builtins__": None, **functions_list}
            result = eval(query, final_sympy_functions)
            return str(result)
        except Exception as e:
            return f"Math Error: {e}"

    def mathematics2(self, query: str):
        try:
            functions_list = {i: getattr(scipy, i) for i in dir(scipy)}
            final_scipy_functions = {"__builtins__": None, **functions_list}
            result = eval(query, final_scipy_functions)
            return str(result)
        except Exception as e:
            return f"Math Error: {e}"
    
    def mathematics3(self, query: str):
        try:
            functions_list = {i: getattr(numpy, i) for i in dir(numpy)}
            final_numpy_functions = {"__builtins__": None, **functions_list}
            result = eval(query, final_numpy_functions)
            return str(result)
        except Exception as e:
            return f"Numpy Error: {e}"
        
math = Mathematics()
math_tool1 = Tool(name="Mathematics1",
            func=math.mathematics1,
            description="""
            This tool evaluates mathematical expressions using SymPy.

            RULES:
            - If user query is messy, extract the math expression yourself and call me. Strictly Do not solve math yourself.
            - If output is "Math Error: ..." you MUST rewrite and retry up to 5 times.
            - Only escalate to Mathematics 2 if repeated retries fail after 5th time.
            - Never give a final refusal if there is any math content.
            - Your job is to clean nonsensical user input, extract math, and solve.
            - you must NOT switch tools or solve directly.
            - Instead, correct the expression (fix typos, add parentheses, use proper function names) 
            and call Mathematics AGAIN with the corrected expression.
            - Do not use LLM Model for math unless every math tool (Mathematics 1, Mathematics 2, Mathematics 3 failed completely) has failed.
            """
        )
math_tool2 = Tool(
            name="Mathematics2",
            func=math.mathematics2,
            description="""
            This tool evaluates Advance mathematical expressions using Scipy.

            RULES:
            - Always call THIS tool for Advance math problems if Mathematics 1 function failed multiple times . Do not solve math yourself.
            - If you see 'Math Error' or symbolic output (like sin(x), cos(x)), 
            you must NOT switch tools or solve directly.
            - Instead, correct the expression (fix typos, add parentheses, use proper function names) 
            and call Mathematics AGAIN with the corrected expression.
            - Repeat correction and retry up to 4 times before escalating to Mathematics 2.
            - Do not use LLM Model for math unless every math tool has failed.
            """)
        
math_tool3 = Tool(
            name="Mathematics3",
            func=math.mathematics3,
            description="""
            This tool evaluates Advance mathematical expressions using numpy.

            RULES:
            - Always call THIS tool for Advance math problems if Mathematics 2 function failed multiple times . Do not solve math yourself.
            - If you see 'Math Error' or symbolic output (like sin(x), cos(x)), 
            you must NOT switch tools or solve directly.
            - Instead, correct the expression (fix typos, add parentheses, use proper function names) 
            and call Mathematics AGAIN with the corrected expression.
            - Repeat correction and retry up to 4 times before escalating to LLM.
            - Do not use LLM Model for math unless every math tool has failed.
            """)