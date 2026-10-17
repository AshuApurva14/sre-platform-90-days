"""
Capture output of the  command

For more theoritical Gyaan:

Refer 👉 01-foundations/week-03-python/day-19-python-subprocess/notes/03-capture-output.md


"""

import subprocess

result = subprocess.run(
    ["df", "-h"],
    capture_output=True,
    text=True
)   

print(result.stdout)