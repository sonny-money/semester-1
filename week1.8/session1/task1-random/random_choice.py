import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
num = int(input("input number of names"))
for i in range(1,num):
    name = names[random.randint(1,len(names))]
    print(name)

# Display the chosen names, one per line
