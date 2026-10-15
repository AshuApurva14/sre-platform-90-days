""" 
Validate all values

"""

def validate_input(value, name):
    if not isinstance(value, (int, float)):
        raise ValueError(f"{name}" must be a number)

    if value < 0 or value > 100:
        raise ValueError(f"{name} value must be in between 0 to 100")

    