"""
Format the output in correct format
"""

def format_resource_status(resource, value, status):
    """ Format the status of one server"""

    return f"{resource:<10}: {value:>5}% [{status}]"


def format_health_report(hostname, cpu, memory, disk, overall):
    """ Build a complete server health report """

    lines = [
        f"Server Health Report: {hostname}",
        "-" * 35,
        format_resource_status("CPU", cpu["value"], cpu["status"]),
        format_resource_status("Memory", memory["value"], memory["status"]),
        format_resource_status("Disk", disk["value"], disk["status"]),
        "-" * 35,
        f"Overall Status: {overall}",
    ]

    return "\n".join(lines)

   