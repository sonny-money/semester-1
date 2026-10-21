"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Sonny Milburn
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }
order = ["red", "red_amber", "green", "amber"]

systime = 0
timeInState = 0
maxtime = int(input("Input max time"))  # read an integer number of steps (>0)
index = 0
state = "red"

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

for i in range(0, maxtime):
    systime += 1
    timeInState += 1
    if timeInState == states[state]:
        index = (index + 1) % len(order)
        state = order[index]
        timeInState = 0
    print(f"Time {systime:03} State {state}")

        


# At the end of each step you should output the time and state using the statement on line 14