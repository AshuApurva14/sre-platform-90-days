"""
Fix wrong mode during file operations using "a" append mode

"""

import requests


url = 'https://httpbin.org/get'
headers = {"Accept": "application/json"}
params = {"name": "Maruti"}

response = requests.get(url, headers=headers, params=params)


filename = "/workspaces/sre-platform-90-days/01-foundations/week-03-python/day-18-python-file-handling/troubleshooting/troubleshoot-02/server.txt"

try:
    with open(filename, "a", encoding="utf-8") as file:
        file.write(response.text)

except FileNotFoundError:
    print("The file does not exists")

