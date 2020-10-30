class Student:
    def __init__(self, name, speciality, subjects, group):
        self.name = name
        self.speciality = speciality
        self.subjects = subjects
        self.group = int(group)

    def __repr__(self):
        return f'{self.name}'