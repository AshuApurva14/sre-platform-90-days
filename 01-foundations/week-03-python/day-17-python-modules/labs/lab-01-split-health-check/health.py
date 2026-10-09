"""
Import validation.py into health.py
"""
from validation import validation_percentage

def check_cpu(cpu):
    validation_percentage(cpu, 'CPU')

    if cpu >= 90:
        return "CRITICAL"
    elif cpu >= 80:
        return "WARNING"
    else:
        return "OK"

def check_memory(memory):
    validation_percentage(memory, 'MEMORY')

    if memory >= 90:
        return "CRITICAL"
    elif memory >= 80:
        return "WARNING"
    else:
        return "OK"

    
    
def check_disk(disk):
    validation_percentage(disk, 'DISK')

    if disk >= 90:
        return "CRITICAL"
    elif disk >= 80:
        return "WARNING"
    else:
        return "OK"


def overall_status(statuses):
    if "CRITICAL" in statuses:
        return "CRITICAL"

    if "WARNING" in statuses:
        return "WARNING"

    return "OK"

