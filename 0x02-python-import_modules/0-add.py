#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum of 1 and 2."""
# Import the add function from add_0.py
from add_0 import add
# Assign values to variables
a = 1
b = 2
# Print the addition result with string formatting
print("{} + {} = {}".format(a, b, add(a, b)))
