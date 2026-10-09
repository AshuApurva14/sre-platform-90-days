"""
Get server details

"""

def get_server_name(server):
    return server["hostname"]

def get_server_ip(server):
    return server["ip"]


def print_server_all_info(server):
    print(f"Server: {server['hostname']}")
    print(f"IP: {server['ip']}")


    