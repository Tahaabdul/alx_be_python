# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert both inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division and check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        # Return the result of the division
        result = num / denom
        return f"The result of the division is {result}"

    # Handle non-numeric inputs
    except ValueError:
        return "Error: Please enter numeric values only."
