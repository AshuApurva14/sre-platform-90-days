"""
Methods.py

"""

class Server:

    def __init__(self, hostname, cpu):
        self.hostname = hostname
        self.cpu = cpu


    def check_cpu(self):
        if self.cpu >= 90:
            return "CRITICAL"
        elif self.cpu >= 80:
            return "WARNING"
        return "OK"


server = Server("web01", 90)
status = server.check_cpu()

print(status)
