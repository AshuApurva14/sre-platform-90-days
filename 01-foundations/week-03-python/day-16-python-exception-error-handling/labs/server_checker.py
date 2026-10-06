"""
Find the health of the system
"""

def check_cpu(cpu):
    if not isinstance(cpu, (int, float)):
        raise ValueError("CPU must be a number")

    if cpu < 0 or cpu > 100:
        raise ValueError("CPU Value must be in between 0-100")
    
    if cpu >= 90:
        return "CRITICAL"
    elif cpu >= 80:
        return "WARNING"
    else:
        return "OK"


def check_memory(memory):
    if not isinstance(memory, (int, float)):
        raise ValueError("Memory must be a number")
    
    if memory < 0 or memory > 100:
        raise ValueError("Memory Value must be in between 0-100")

    if memory >= 90:
        return "CRITICAL"
    elif memory >= 80:
        return "WARNING"
    else:
        return "OK"

def check_disk(disk):
    if not isinstance(disk, (int, float)):
        raise ValueError("Disk must be a number")

    if disk < 0 or disk > 100:
        raise ValueError("Disk value must be in between 0-100")

    if disk >= 90:
        return "CRITICAL"
    elif disk >= 80:
        return "WARNING"
    else:
        return "OK"

def overall_status(statuses):

    if "CRITICAL" in statuses:
        return "CRITICAL"
    elif "WARNING" in statuses:
        return "WARNING"
    else:
        return "OK"




def check_server(server):
    try:
        hostname = server["hostname"]
        cpu = server["cpu"]
        memory = server["memory"]
        disk = server["disk"]

        cpu_status = check_cpu(cpu)
        memory_status = check_memory(memory)
        disk_status = check_disk(disk)
    
        statuses = [
                cpu_status, 
                memory_status, 
                disk_status
                ]

        overall = overall_status(statuses)


        print("===============================================")
        print(" SERVER HEALTH ")
        print("===============================================")


        print(f"\nHostname: {hostname}")


        print(f"\nCPU: {cpu}% [{cpu_status}]")
        print(f"MEMORY: {memory}% [{memory_status}]")
        print(f"DISK: {disk}% [{disk_status}]")

        print(f"\nOverall status: {overall}")

        print(f"\n============================================")

    except KeyError as error:
        print(f"ERROR: Missing server information: {error}")

    except ValueError as error:
        print(f"ERROR: Invalid server data: {error}")


server = {

     "hostname": "Server1",
     "cpu": "eighty",
     "memory": 78,
     "disk": 80
   }

check_server(server)