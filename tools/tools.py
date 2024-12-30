from langchain_community.tools.tavily_search import TavilySearchResults

def get_linkedin_profile_url_tavily(name: str):
    """Searches for linkedin or twitter profile page"""
    
    search = TavilySearchResults()
    res = search.run(f'{name}"s twitter profile')
    return res


def get_twitter_profile_url_tavily(name: str):
    """Searches for linkedin or twitter profile page"""
    
    search = TavilySearchResults()
    res = search.run(f'{name}"s  twitter profile')
    return res


# print(get_profile_url_tavily("Dewesh Pandey iitg linkedin profile"))