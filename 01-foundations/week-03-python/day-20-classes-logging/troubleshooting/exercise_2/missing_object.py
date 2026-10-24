"""
Missing object

"""

class Server:
    def __init__(self, hostname):
        self.hostname = hostname

    def show(self):
        print(self.hostname)


Server = Server("web01")

print(Server)