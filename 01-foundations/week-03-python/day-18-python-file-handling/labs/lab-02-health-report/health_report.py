hostname = "web01"
cpu = 85
memory = 70
disk = 80

report = f"""
Server Health Report
--------------------
Hostname: {hostname}
CPU: {cpu}%
Memory: {memory}%
Disk: {disk}%
"""

with open("/workspaces/sre-platform-90-days/01-foundations/week-03-python/day-18-python-file-handling/labs/lab-02-health-report/health-report.txt", "w") as file:
    file.write(report)

print("Health Report Created.")




