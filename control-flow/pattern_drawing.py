# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))
row = size  # Initialize row with the size

# Check if the input is positive
if size > 0:
    # Draw the pattern
    while row > 0:
    # Print a row of asterisks without moving to a new line
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after completing a row
        row -= 1  # Decrement the row counter
else:
    print("Please enter a positive integer.")