# Worksheet 1.2: Task 2 Solution
import sys

adding = True
nums = []

while adding:
    try:
        num = float(input("Input a float or type any letter to exit"))
        nums.append(num)
    except ValueError:
        adding = False
    

if len(nums) == 0:
    sys.exit("Error: no numbers provided")
else:
    print(nums)