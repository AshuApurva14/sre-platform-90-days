from health import check_cpu, check_memory, check_disk, overall_status

def main():

    server = {

        "hostname": "Server1",
        "cpu": 80,
        "memory": 88,
        "disk": 96
    }


    try:

        cpu_status = check_cpu(server["cpu"])
        memory_status = check_memory(server["memory"])
        disk_status = check_disk(server["disk"])

        statuses = {
            cpu_status,
            memory_status,
            disk_status
        }


        overall = overall_status(statuses)

        print("===============================================")
        print("SERVER HEALTH CHECK")
        print("===============================================")

        print(f"\nHostname: {server['hostname']}")

        print(f"\nCPU: {server['cpu']}% [{cpu_status}]")
        print(f"Memory: {server['memory']}% [{memory_status}]")
        print(f"Disk: {server['disk']}% [{disk_status}]")

        print(f"\nOverall status: {overall}")

        print(f"\n============================================")

    except (KeyError, ValueError) as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
