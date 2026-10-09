"""
Check CPU, Mmeory and Disk usages
"""

from validation import validate_input

def check_cpu(cpu):
    validate_input(cpu, "CPU")

    if cpu >= 90:
        return "CRITICAL"

    elif cpu >= 80:
        return "WARNING"

    else:
        return "OK"



def check_memory(memory):
    validate_input(memory, "MEMORY")

    if memory >= 90:
        return "CRITICAL"
    elif memory >= 80:
        return "WARNING"
    else:
        return "OK"

def check_disk(disk):
    validate_input(disk, "DISK")

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

    