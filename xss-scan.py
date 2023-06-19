import requests
from bs4 import BeautifulSoup
import re

def xss_vulnerability_scanner(url):
    # send HTTP request to the provided URL and save the response from the server in a response object called r
    r = requests.get(url)

    # create a BeautifulSoup object
    soup = BeautifulSoup(r.text, 'html.parser')

    # find all input tags and textarea tags on the webpage
    inputs = soup.find_all(['input', 'textarea'])

    # return a message if no input or textarea tags are found
    if len(inputs) == 0:
        return "No input or textarea tags found on the webpage."

    xss_payload = "<script>alert('XSS Vulnerability!');</script>"

    for input in inputs:
        input_name = input.get('name')
        input_type = input.get('type')

        if input_type != 'hidden':
            post_data = {input_name: xss_payload}
            target_url = url

            if re.match(r'^https?://', target_url) is None:
                target_url = f'http://{target_url}'

            r = requests.post(target_url, data=post_data)

            # check if the payload is reflected in the response HTML
            if xss_payload in r.text:
                return f"[!] The website {url} is vulnerable to XSS (Cross-Site Scripting)."

    return f"[+] The website {url} is secure."

url = input("Enter the URL to scan: ")
print(xss_vulnerability_scanner(url))
