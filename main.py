import requests
import json

github_base_url = "https://api.github.com"

user = input("enter the gh user: ")

s = requests.Session()

response = s.get(f"{github_base_url}/users/{user}/repos")

#load response via json.loads as it is a string response
projects = json.loads(response.text)


for project in projects:
    print(f"Project name: {project['name']}")
    print(f"URL: {project['html_url']}\n")
    