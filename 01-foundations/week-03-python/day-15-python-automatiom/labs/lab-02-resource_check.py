"""
Resource utilization tool

"""

def resource_check(name, usage):
    if usage >= 90:
        return f"{name}: {usage}% CRITICAL"
    elif usage >= 80:
        return f"{name}: {usage}% WARNING"
    else:
        return f"{name}: {usage}% OK"


cpu = 95
memory = 70
disk = 73

print(resource_check("CPU", cpu))
print(resource_check("MEMORY", memory))
print(resource_check("DISK", disk))

