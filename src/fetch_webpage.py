import requests 

def fetch_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f'\n\tFailed to fetch web page: {url}.\n\tStatus code: {response.status_code}\n')
    
# Good
# url = "https://worldpopulationreview.com/countries/italy"
# page_content = fetch_page_content(url)