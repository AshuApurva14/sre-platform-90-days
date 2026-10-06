"""
A health check tool with validating all input values.

"""

def check_cpu(cpu):
    if cpu >= 90:
        return "CRITICAL"
    elif cpu >= 80:
        return "WARNING"
    else:
        return "OK"

def check_memory(memory):

    if memory >= 90:
        return "CRITICAL"
    elif memory >= 80:
        return "WARNING"
    else:
        return "OK"

def check_disk(disk):

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

def  main():

    try:
        hostname = input("Enter the hostname: ")
        cpu = int(input("Enter the CPU usages: "))
        memory = int(input("Enter the MEMORY usages: "))
        disk = int(input("Enter the DISK usages: "))

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
            

    except ValueError:
        print("ERROR: Resources usages values must be valid value [For ex:- Hostname: server2, CPU: 90, MEMORY: 80, DISK: 70]")

if __name__ == "__main__":
    main()



