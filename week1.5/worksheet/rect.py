# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)

        if not isinstance(width, int):
            raise TypeError("Width must be an integer")
        if not isinstance(height, int):
            raise TypeError("Height must be an integer")
        if height <= 0 or width <= 0:
            raise ValueError("Values must be greater than zero")

        self.width = width
        self.height = height

    def is_square(self):
        '''
        Returns true if shape is a square, false if otherwise
        '''
        if self.width == self.height:
            return True
        else:
            return False

    def area(self):
        '''
        Returns the area of the shape
        '''
        return self.height * self.width

    def perimeter(self):
        '''
        Returns the perimeter of the shape
        '''
        return (2*self.height) + (2*self.width)

