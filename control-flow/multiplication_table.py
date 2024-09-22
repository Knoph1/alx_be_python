# multiplication_table.py

# Prompt user for input
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to generate and print the multiplication table from 1 to 10
for i in range(1, 11):
    # Calculate the product
    product = number * i
    # Print the multiplication in the format "X * Y = Z"
    print(f"{number} * {i} = {product}")
