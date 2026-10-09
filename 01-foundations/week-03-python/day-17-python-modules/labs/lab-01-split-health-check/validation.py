"""
Validation.py
"""

def validation_percentage(value, name):
    if not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be number")

    if value < 0 and value > 100:
        raise ValueError(f"{name} must be between 0 to 100")

    