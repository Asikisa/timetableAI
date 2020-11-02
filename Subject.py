class Subject:
    def __init__(self, name, subj_type, enrolled_students, teacher):
        self.name = name
        self.subj_type = subj_type
        self.teacher = teacher
        # self.enrolled_students_first_group = enrolled_students_first_group
        self.enrolled_students = enrolled_students

    def get_num_of_students(self):
        return len(self.enrolled_students)

    def __repr__(self):
        return "subject: '" + self.name + ", " + self.subj_type + ", teacher: " + self.teacher.name + "'"

    def __eq__(self, other):
        if isinstance(other, Subject):
            return self.__key() == other.__key()
        return NotImplemented

    def __key(self):
        return self.name, self.subj_type

    def __hash__(self):
        return hash(self.__key())