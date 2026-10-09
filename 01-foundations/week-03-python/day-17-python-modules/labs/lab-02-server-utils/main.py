"""
Import server utils and get the server details

"""

from server_utils import get_server_name, get_server_ip, print_server_all_info


server = {
    "hostname": "Server1",
    "ip": "192.168.98.12"
}

# print(get_server_name(server))
# print(get_server_ip(server))

print_server_all_info(server)

