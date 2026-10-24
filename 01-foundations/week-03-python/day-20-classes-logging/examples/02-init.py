class Server:

    def __init__(self, hostname, cpu, memory, disk):
        self.hostname = hostname
        self.cpu = cpu
        self.memory = memory
        self.disk = disk




server = Server(
    "Web01",
    85,
    89,
    78
)


print(server.hostname)
print(server.cpu)
print(server.memory)
print(server.disk)

