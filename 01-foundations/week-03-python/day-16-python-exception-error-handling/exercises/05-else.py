try:
    number = int("a")

except ValueError:
    print("Invalid number")

else:
    print(f"Valid number: {number}")