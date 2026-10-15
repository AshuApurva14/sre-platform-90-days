"""
Fix the problem of file closed after file operations

"""

filename = "/workspaces/sre-platform-90-days/01-foundations/week-03-python/day-18-python-file-handling/troubleshooting/troubleshoot-03/file_not_closed.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:

        file.read()

    # print(file.read())

    print("File coontent read is done")

except ValueError:
    print("I/O operation on closed file")