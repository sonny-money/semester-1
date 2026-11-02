# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
from shapes import Shape

class Circle(Shape):
    def __init__(self):
        super().__init__((5,5),"red")
    