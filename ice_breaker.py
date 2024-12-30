import os 
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate # for prompt template class object to convert user input + parameters into instruction for LLM model to understand
from langchain_core.output_parsers import StrOutputParser # to convert the AImessage output of the LLM model into string of message i.e. more usable format
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
# Class to  chain the LLM model with hte user instruction or prompt
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from output_parsers import summary_parser, Summary
from typing import Tuple

def ice_break_with(name: str) -> Tuple[Summary, str]:
    
    linkedin_username = linkedin_lookup_agent(name= name)
    linkedin_data = scrape_linkedin_profile( linkedin_profile_url = linkedin_username)
    
    twitter_username = twitter_lookup_agent(name = name)
    tweets = scrape_user_tweets(username= twitter_username[1:] )
    
    summary_template = """
        Given the information about a person fron Linkedin {information},
        and latest twitter posts {twitter_posts} I want you to create:
        1. a short summary
        2. two interesting facts about them
        
        use both information from LinkedIn and Twitter
        \n{format_instructions}
    """
    
    
    summary_prompt_template = PromptTemplate(
        input_variables =[ "information", "twitter_posts"], template= summary_template,
        partial_variables= {"format_instructions": summary_parser.get_format_instructions()}
    )  #   the PromptTemplate Object wih template as "summary_template" strning and "nformation" as parameter
    
    llm = ChatOpenAI(temperature=0 , model_name= "gpt-3.5-turbo") # loading the LLM model and defining the temperature for the randomness
    
    # chain = summary_prompt_template | llm | StrOutputParser()   # chaining or joining or integrating the prompttemplate object with the llm model and suggesting the output format
    chain = summary_prompt_template | llm | summary_parser
    
    # linkedin_data = scrape_linkedin_profile(linkedin_profile_url= "https://www.linkedin.com/in/eden-marco")
    
    res: Summary =  chain.invoke( input = { "information": linkedin_data, "twitter_posts" : tweets}) # invoking the chain with information and storing in the res the output message from LLM , since hte StrOutputParser is used the output is not AImessgae raather a represenatable string
    print()
    
    # print(res)
    return res, linkedin_data.get("profile_pic_url")
    

if __name__ == '__main__':
    load_dotenv() # loading the environment variables
    print("Ice Breaker")
    os.environ["OPENAI_API_KEY"]    # OPENAI API key 
    
    ice_break_with(name= "Eden Marco")
    
    # summary_template = """
    #     given the LinkedIn information {information} about a person from I want you to create:
    #     1. a short summary
    #     2. two interesting facts about them
    # """
    
    
    # summary_prompt_template = PromptTemplate(
    #     input_variables =[ "information"], template= summary_template
    # )  # creating the PromptTemplate Object wih template as "summary_template" strning and "nformation" as parameter
    
    # llm = ChatOpenAI(temperature=0 , model_name= "gpt-3.5-turbo") # loading the LLM model and defining the temperature for the randomness
    
    # chain = LLMChain( llm = llm , prompt = summary_prompt_template)
    # print( chain.run(information = information))
    
    # chain = summary_prompt_template | llm | StrOutputParser()   # chaining or joining or integrating the prompttemplate object with the llm model and suggesting the output format
    
    # linkedin_data = scrape_linkedin_profile(linkedin_profile_url= "https://www.linkedin.com/in/eden-marco")
    
    # res =  chain.invoke( input = { "information": linkedin_data}) # invoking the chain with information and storing in the res the output message from LLM , since hte StrOutputParser is used the output is not AImessgae raather a represenatable string
    # print()
    
    # print(res)
    
    