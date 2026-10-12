# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers 

total = 0
nums = read_numbers()

if len(nums) == 0:
    sys.exit("Error: no numbers provided")

for item in nums:
    total = total + item

nums.sort()


mean = total / len(nums)
max = max(nums)
min = min(nums)
median = nums[len(nums)//2]

print(f"Minimum = {min}")
print(f"Maximum = {max}")
print(f"Mean = {mean}")
print(f"Median = {median}")