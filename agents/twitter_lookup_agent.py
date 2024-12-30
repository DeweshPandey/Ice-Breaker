import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
     create_react_agent,
     AgentExecutor,
)
from langchain import hub
from tools.tools import get_twitter_profile_url_tavily

load_dotenv()

def lookup( name:str) -> str:
    llm = ChatOpenAI(
        temperature = 0,
        model_name = "gpt-4o"
    )
    template = """
    Given the name {name_of_person} I want you to find a link to their Twitter profile page, and extract from it their username
    In your final answer only person's username 
    """
    
    prompt_template = PromptTemplate(
        template = template , input_variables = ["name_of_person"]
    )
    
    
    tools_for_agent = [
        Tool(
            name = "Crawl Google 4 Twitter Profile Page", 
            func = get_twitter_profile_url_tavily,
            description= "useful for when you need to get Twitter Page URL",
        )
    ]
    
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent( llm = llm , tools = tools_for_agent , prompt = react_prompt)
    agent_executor = AgentExecutor( agent = agent, tools= tools_for_agent , verbose = True)
    
    result = agent_executor.invoke(
        input = {'input': prompt_template.format_prompt(name_of_person=name)}
    )
    
    twitter_profile_username = result['output']
    return twitter_profile_username
    
if __name__== '__main__':
    twitter_username = lookup( name= "Eden Marco")
    print(twitter_username)