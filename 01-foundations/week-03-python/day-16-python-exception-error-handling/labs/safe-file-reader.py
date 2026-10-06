"""
Check file exists or not? If yes , then Read a file and if not then raise a error
"""
from pathlib import Path

file_path = Path("/workspaces/sre-platform-90-days/01-foundations/week-03-python/day-16-python-exception-error-handling/application.log")

try:
    with open(file_path, "r") as file:
        content = file.read()
    print(content)

except FileNotFoundError:
    print("ERROR: application.log does not exist")

