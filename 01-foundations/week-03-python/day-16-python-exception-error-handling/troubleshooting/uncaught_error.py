# Bug code

cpu = "85"

print(cpu + 10)

# Here issue is that variable cpu is string and it is trying to add integer

# Correct Solution

cpu = 85

try:
    if isinstance(cpu, (str)):
        raise ValueError("CPU value must be a number")

except ValueError as error:
    print(f"Invalid Value: {error}")

else:
   print(cpu + 10)

