import sys
import time
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/json',

    }

def send_request(id:int, h:dict)->bool:
    """
    Send a request
    """
    url = "https://niccs.cisa.gov/workforce-development/nice-framework/task/t"+str(id)
    print(url)
    response = requests.get(url, headers=h, timeout=2)
    if response.status_code < 200 or response.status_code > 399:
        print(response)
        sys.exit(1)

   
    return response

r = send_request(2000, headers)
