"""
Implement command runner class

"""

class Server:

    def __init__(self, hostname, cpu, memory, disk):
        self.hostname = hostname
        self.cpu = cpu
        self.memory = memory
        self.disk = disk

    def check_cpu(self):
        if self.cpu >= 90:
            return  "CRITICAL"
        elif self.cpu >= 80:
            return "WARNING"
        return "OK"

    def check_memory(self):
        if self.memory >= 90:
            return "CRITICAL"
        elif self.memory >= 80:
            return "WARNING"
        return "OK"

    def check_disk(self):
        if self.disk >= 90:
            return "CRITICAL"
        elif self.disk >= 80:
            return "WARNING"
        return "OK"

    def overall_status(self):
        if self.check_cpu() == "CRITICAL" or self.check_memory() == "CRITICAL" or self.check_disk() == "CRITICAL":
            return "CRITICAL"
        elif self.check_cpu() == "WARNING" or self.check_memory() == "WARNING" or self.check_disk() == "WARNING":
            return "WARNING"
        return "OK"
    


server = Server(
    hostname="Web01",
    cpu=89,
    memory=90,
    disk=78
)




print(server.check_cpu())
print(server.check_memory())
print(server.check_disk())
print(server.overall_status())

