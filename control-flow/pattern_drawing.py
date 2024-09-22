# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the number of rows
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in the row
    for column in range(size):
        print("*", end="")  # Print asterisk without a newline

    # Move to the next line after the row is complete
    print()  # This adds a newline after each row

    # Increment the row counter
    row += 1
