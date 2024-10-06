# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    # Ensure the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Retrieve the command-line arguments (numerator and denominator)
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform the division using safe_divide function
    result = safe_divide(numerator, denominator)

    # Output the result or error message
    print(result)

if __name__ == "__main__":
    main()
