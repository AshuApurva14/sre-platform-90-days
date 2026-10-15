"""
File handler method

"""

def read_servers(filename):
    servers = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split(",")

            server = {
                "hostname": parts[0],
                "cpu": int(parts[1]),
                "memory": int(parts[2]),
                "disk": int(parts[3])
            }

            servers.append(server)

    return servers


def write_report(filename,  report):
    with open(filename, "w") as file:
        file.write(report)





