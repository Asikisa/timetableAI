class Subject:
    def __init__(self, name, type, enrolled_students, teacher):
        self.name = name
        self.type = type
        self.teacher = teacher
        # self.enrolled_students_first_group = enrolled_students_first_group
        self.enrolled_students = enrolled_students

    def get_num_of_students(self):
        return len(self.enrolled_students)

    def __repr__(self):
        return "subject: '" + self.name + "'"

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)