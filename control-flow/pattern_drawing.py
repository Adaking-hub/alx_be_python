# pattern_drawing.py
# Pattern drawing using while loop and nested for loop

# Prompt User for Pattern Size
pattern = int(input("Enter the size of the pattern: "))

# Validate input (optional)
if pattern <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    while row < pattern:
        for col in range(pattern):
            print("*", end="")  # Print asterisk without newline
        print()  # Move to the next line after each row
        row += 1