destination = input("where are you going? ")
distance = int(input("how many miles? "))
time = float(input("how many hours will the journey take"))

avg_speed = distance/time

print(f"the average speed to travel to {destination} is {avg_speed} miles per hour")