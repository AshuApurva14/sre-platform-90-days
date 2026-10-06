"""
This program asks for usr input to check system resources.
"""

try:
    cpu_usages = int(input("Enter CPU Usages: "))
except ValueError:
    print(f"Invalid : Enter a valid number between 0 to 100")
    raise SystemExit(2)

    
if not 0 <= cpu_usages <= 100:
    print("Invalid input: CPU Usages must be between 0 and 100")    
    raise SystemExit(2)
print(f"CPU Usages: {cpu_usages}%")
    
