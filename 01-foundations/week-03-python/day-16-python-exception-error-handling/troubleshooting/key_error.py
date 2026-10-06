"""
Handle Key Error

"""

server = {
    "hostname": "server01",
    "memory": 75,
    "disk": 92
}

try:
    cpu = server["cpu"]
    
except KeyError as error:
    print(f"KeyError: {error} is missing")

else:
    print(f"CPU usages: {cpu}%")