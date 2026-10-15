"""
Open file and read
"""

file = open('/workspaces/sre-platform-90-days/01-foundations/week-03-python/day-18-python-file-handling/examples/sample.txt', 'r')

content = file.read()

print(content)

file.close()

