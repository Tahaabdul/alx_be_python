# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Check if the input is positive
if size > 0:
    # Draw the pattern
    for row in range(size):
        print("*" * size)  # Print a row of asterisks
else:
    print("Please enter a positive integer.")