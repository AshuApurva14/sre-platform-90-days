"""
Check server status


"""

hostname = "server-1"
status = "DOWN"

print("==============================")
print("SERVER STATUS")
print("==============================")

if status == "UP":
   print(f"{hostname} is healthy")
else:
    print(f"{hostname} required attention")




