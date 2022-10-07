"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

length = len(numbers)
numbers.sort()

median = None
c = int(length / 2)

if length % 2 == 0:
    a = numbers[c]
    b = numbers[c - 1]
    median = float((a + b) / 2.0)
else: 
    median = numbers[c]

print(median)