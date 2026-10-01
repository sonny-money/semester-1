import sys

"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Sonny Milburn
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
try:
    amount = int(input("how much money do you want to save per month? "))
except ValueError:
    print("Enter a valid integer!")
    sys.exit()
    
# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

print(f"You will save £{round(float(amount * 12), 2)} per year, without interest.")
# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

print(f"You will save £{round(float((amount*12) * 1.008),2)} per year, with interest.")
