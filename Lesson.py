class Lesson:
    def __init__(self, num_of_lesson, subject, teacher, audience):
        self.num_of_lesson = num_of_lesson
        # self.type_of_lesson = type_of_lesson
        # self.num_of_group = num_of_group
        self.subject = subject
        self.teacher = teacher
        self.audience = audience

    def __repr__(self):
        if self.type_of_lesson == 'lecture':
            return f'{self.num_of_lesson} {self.subject} {self.teacher} {self.audience}'
        else:
            return f'{self.num_of_lesson} {self.subject} {self.teacher} {self.audience}'
