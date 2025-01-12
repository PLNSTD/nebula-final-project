import requests 

def fetch_page_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            raise Exception(f'\n\tFailed to fetch web page: {url}.\n\tStatus code: {response.status_code}\n')
    except Exception as e:
        print(e)
    return None