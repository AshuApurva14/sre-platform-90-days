"""
Read file with for loop

"""

with open("/workspaces/sre-platform-90-days/01-foundations/week-03-python/day-18-python-file-handling/examples/sample.txt", "r") as file:
    for line in file:
        server = line.strip()
        print(server)
