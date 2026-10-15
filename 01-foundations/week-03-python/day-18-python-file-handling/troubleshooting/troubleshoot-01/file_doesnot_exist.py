"""
To fix the issue related to "file doesn't exists"

"""

filename = "production.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

except FileNotFoundError:
    print("The file was not found")