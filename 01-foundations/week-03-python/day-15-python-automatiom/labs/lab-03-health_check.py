"""
Find the health of the system
"""

def check_cpu(cpu):
    if cpu >= 90:
        return f"CPU usages: {cpu}% CRITICAL"
    elif cpu >= 80:
        return f"CPU usages: {cpu}% WARNING"
    else:
        return f"CPU usages: {cpu}% OK"


def check_memory(memory):

    if memory >= 90:
        return f"CPU usages: {memory}% CRITICAL"
    elif memory >= 80:
        return f"CPU usages: {memory}% WARNING"
    else:
        return f"CPU usages: {memory}% OK"

def check_disk(disk):

    if disk >= 90:
        return f"CPU usages: {disk}% CRITICAL"
    elif disk >= 80:
        return f"CPU usages: {disk}% WARNING"
    else:
        return f"CPU usages: {disk}% OK"

def overall_status(statuses):

    return statuses

def main():

    hostname = "server01"

    cpu = 89
    memory = 88
    disk = 78

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


if __name__ == "__main__ ":
    main()