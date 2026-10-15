"""
Read file server.txt and fetch the list of servers
"""


def read_servers(filename):

    try:
        with open(filename, "r") as file:
            for line in file:
                server = line.strip()

                if server:
                   print(f"checking server: {server}")

    except FileNotFoundError:
        print(f"ERROR: File {filename} was not found")


read_servers("/workspaces/sre-platform-90-days/01-foundations/week-03-python/day-18-python-file-handling/labs/lab-01-server-list/server_old.txt") 