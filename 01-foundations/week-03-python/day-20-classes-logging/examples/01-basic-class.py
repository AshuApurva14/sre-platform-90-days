"""
Basic class definition


"""

class Server:
    def __init__(self, hostname):
        self.hostname = hostname
        

server1 = Server("Web01")
server2 = Server("db01")

print(server1.hostname)
print(server2.hostname)

