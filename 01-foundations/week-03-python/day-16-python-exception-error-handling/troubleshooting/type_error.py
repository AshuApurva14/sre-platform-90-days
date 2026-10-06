"""
Handle type error 

"""

# Example 1

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError as error:
    print(f"Invalid input: {error}")
else:
    print(f"Age accepted: {age}")


# Example 2


server = {

     "hostname": "Server1",
     "cpu": "ninty-nine",
     "memory": 78,
     "disk": 80
}

cpu = server["cpu"]

if not isinstance(cpu, (int, float)):
    raise TypeError("CPU must be a number")

try:

    if cpu >= 90:
        print("CRITICAL")
    elif cpu >= 80:
        print("WARNING")
    else:
        print("OK")

except TypeError:
    print("ERROR: CPU value must be a number")

