# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name:str, birth:date):
        '''
        creates a person with a name, date of birth
        '''
        if not isinstance(name,str):
            raise TypeError("Name must be a string")
        if name == "":
            raise ValueError("Name cannot be an empty string")
        if not isinstance(birth, date):
            raise TypeError("birth must be a date object")
        self.name = name
        self.birth = birth

    def initials(self):
        '''
        Produce a string of initials, from the given name
        '''

        initial = ""
        for word in self.name.split():
            initial += word[0].upper()
        return initial

    def is_birthday(self):
        '''
        Check if the persons birth is today
        '''
        today = date.today()

        if self.birth.day == today.day and self.birth.month == today.month:
            return True
        else:
            return False

