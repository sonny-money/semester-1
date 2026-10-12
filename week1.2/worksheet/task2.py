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

if len(nums) % 2 == 1:
    median = nums[len(nums)//2]
else:
    median = (nums[(len(nums)//2)] + nums[(len(nums)//2) - 1]) / 2

mean = total / len(nums)
maximum = max(nums)
minimum = min(nums)

print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")