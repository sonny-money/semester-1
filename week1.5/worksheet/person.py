# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name:str, birthday:date):
        if not isinstance(name,str):
            raise TypeError("Name must be a string")
        if name == "":
            raise ValueError("Name cannot be an empty string")
        if not isinstance(birthday, date):
            raise TypeError("Birthday must be a date object")
        self.name = name
        self.birthday = birthday

    def initials(self):
        '''
        Produce a string of initials, from the given name
        '''

        initial = ""
        for char in self.name:
            if char.isupper():
                initial = initial + char
        return initial

    def is_birthday(self):
        '''
        Check if the persons birthday is today
        '''

        if self.birthday == date.today():
            return True
        else:
            return False

