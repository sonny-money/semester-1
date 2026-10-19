# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

sequence = []

prev = 0

for k in range(0, L):
    new = prev - k
    if new > 0 and sequence.count(new) == 0:
        sequence.append(new)
    else:
        new = prev + k
        sequence.append(new)
    prev = sequence[-1]

# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence