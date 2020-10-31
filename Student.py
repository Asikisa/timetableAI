class Student:
    def __init__(self, name, speciality, subject_names, group):
        self.name = name
        self.speciality = speciality
        self.subject_names = subject_names
        self.group = int(group)

    def __repr__(self):
        return f'{self.name}'