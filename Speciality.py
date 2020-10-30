class Speciality:
    def __init__(self, name, number_of_students):
        self.name = name
        self.number_of_students = number_of_students

    def __repr__(self):
        return f'{self.name}'
