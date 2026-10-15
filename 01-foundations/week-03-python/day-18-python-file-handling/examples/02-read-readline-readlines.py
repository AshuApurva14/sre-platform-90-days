"""
Learn and understand read(), readline(), readlines()

"""

# read() 

with open('/workspaces/sre-platform-90-days/01-foundations/week-03-python/day-18-python-file-handling/examples/sample.txt', 'r') as file:
    content = file.read()

print(content)


# readline() - Reads first line

with open('/workspaces/sre-platform-90-days/01-foundations/week-03-python/day-18-python-file-handling/examples/sample.txt', 'r') as file:
    print("This is readline results")
    content = file.readline()

print(content)


# readines() - Reads lines with new line


with open('/workspaces/sre-platform-90-days/01-foundations/week-03-python/day-18-python-file-handling/examples/sample.txt', 'r') as file:
    content = file.readlines()

print(content)


