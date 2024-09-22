# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))
row = size  # Initialize row with the size

# Check if the input is positive
if size > 0:
    # Draw the pattern
    while row > 0:
        print("*" * size)  # Print a row of asterisks
        row -=1
    
else:
    print("Please enter a positive integer.")