# Worksheet 1.2: Task 1 Solution

import sys

try:
    grade = int(input("Input grade 0-100: "))
    if grade < 0 or grade > 100:
        sys.exit("Error: Grade must be an integer between 0 and 100")
except ValueError:
    sys.exit("Error: Grade must be an integer between 0 and 100")

result = ""

if grade <= 39:
    result = "Fail"
elif grade > 39 and grade <= 69:
    result = "Pass"
elif grade > 69:
    result = "Distinction"

print(f"{grade} is a {result}")
