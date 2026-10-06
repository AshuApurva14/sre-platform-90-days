"""
Handle ValueError as a SRE

"""

server = {
    "hostname": "server01",
    "cpu": 150,
    "memory": 75,
    "disk": 92
}

cpu = server["cpu"]

try:
    if cpu < 0 or cpu > 100:
       raise ValueError("CPU value must be between 0-100")

except ValueError as error:
    print(f"Invalid business/application data : {error}")

else:
    if cpu >= 90:
            print("CRITICAL")
    elif cpu >= 80:
            print("WARNING")
    else:
            print("OK")