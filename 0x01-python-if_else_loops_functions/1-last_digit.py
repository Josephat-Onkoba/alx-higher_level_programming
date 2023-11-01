#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = abs(number) % 10

# Determine if the last digit is greater than 5, 0, or less than 6 and not 0
if last_digit > 5:
    comparison = "is greater than 5"
elif last_digit == 0:
    comparison = "is 0"
else:
    comparison = "is less than 6 and not 0"

# Print the result
print(f"The string Last digit of {number} is {last_digit} and {comparison}")
