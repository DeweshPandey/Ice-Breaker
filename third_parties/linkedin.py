
# a Python package has been created named Third_parties as it contains the python special file __init__.py
# a package is collection of useful libraries and modules 
# similarly a module has been created namely linkedin.py with scrape_linkedin_profile function to direclty scrape the linkedin profile for given linkedIn profile ID

import os # to access environment variables
import requests # to make http request through and API that will get the linkedin informaiton
from dotenv import load_dotenv # to load the environment variables

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url:str, mock:bool=True):
    """_summary_

    Args:
        linkedin_profile_url (str): _description_
        mock (bool, optional): _description_. Defaults to False.
    
    scrape information from LinkedIn prfiles,
    Manually scrape the infromation from the LinkedIn profile   
    
    the function will use a LinkedIn profile URL, and with the help of third party API  "Proxyvurl API" to scrape the linkedIN informaiton

    """
    
    if mock : # it tell that if the mock is true then we wont be using the available free credits of Proxycurl and will be using the gist github file for reference
        linkedin_profile_url = "https://gist.githubusercontent.com/DeweshPandey/a2bf97f55a079a604ff4915d07b244f7/raw/ff63fc9042622fc54be2e749e4647250a4a7a666/marco_linkedin.json" 
        # a variable to store the linkedin url or the url of .json file raw
        response = requests.get(
            linkedin_profile_url,
            timeout= 10
        ) # a respone variable store the output from request to fetch the linkedIn profile from given url
        
    else:
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin' # this defines the API endpoint that will be called to retrieve information from Proxycurl LinkedIn Person profile API
        # the following code is as per the snippet given in Proxycurl person profile code to get the response for given linkedin url
        
        headers = {'Authorization': f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}  # a dictionary defining headers sent with HTTP request
        # Authorization: this header required by the API to authenticate the request. It uses a Bearer token
        # request.get() this send the HTTP GET request to the specified endpoint
        response = requests.get(api_endpoint,
                                params= { "url" : linkedin_profile_url},
                                headers=headers,
                                tieout=10)
        
    data = response.json()
    # retrieve the json file 
    data = {
        k:v
        for k , v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    } # remove unnecessary data and empty null fields
    
    if data.get("groups"):
        for group_dict in data.get('groups'):
            group_dict.pop("profile_pic_url")
    
    return data
    
    
    
if __name__ == '__main__' :
    print(
        scrape_linkedin_profile(
            linkedin_profile_url= "https://www.linkedin.com/in/eden-marco")
    )
    