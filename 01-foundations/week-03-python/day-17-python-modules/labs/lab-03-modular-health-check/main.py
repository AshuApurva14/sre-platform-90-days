
from health.checks import (
    check_cpu,
    check_memory,
    check_disk,
    overall_status,
)
from utils.formatter import format_health_report


def main():
    server = {
        "hostname": "server01",
        "cpu": 85,
        "memory": 75,
        "disk": 92,
    }

    try:
        cpu_status = check_cpu(server["cpu"])
        memory_status = check_memory(server["memory"])
        disk_status = check_disk(server["disk"])

        statuses = [cpu_status, memory_status, disk_status]
        overall = overall_status(statuses)

        report = format_health_report(
            hostname=server["hostname"],
            cpu={"value": server["cpu"], "status": cpu_status},
            memory={"value": server["memory"], "status": memory_status},
            disk={"value": server["disk"], "status": disk_status},
            overall=overall,
        )

        print(report)

    except (KeyError, ValueError) as error:
        print(f"ERROR: {error}")


if __name__ == "__main__":
    main()