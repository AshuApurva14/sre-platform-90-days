"""
Using "a" mode in file handling.

"""

import requests


url = 'https://httpbin.org/get'
headers = {"Accept": "application/json"}
params = {"name": "Maruti"}

response = requests.get(url, headers=headers, params=params)

filename = "/workspaces/sre-platform-90-days/01-foundations/week-03-python/day-18-python-file-handling/examples/sample.log"

with open(filename, "a", encoding="utf-8") as file:

    file.write(response.text)

print("Logs file created.")
