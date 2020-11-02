class Lesson:
    def __init__(self, day, num_of_lesson, subject, audience):
        self.day = day;
        self.num_of_lesson = num_of_lesson
        # self.num_of_group = num_of_group
        self.subject = subject
        self.audience = audience

    def __repr__(self):
        return f'{self.subject.name} {self.subject.subj_type} {self.day} {self.num_of_lesson}  {self.subject.teacher} {self.audience}'


class EmptyLesson:

    def __init__(self, day, num_of_lesson):
        self.day = day;
        self.num_of_lesson = num_of_lesson

    def __key(self):
        return self.day, self.num_of_lesson

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, EmptyLesson):
            return self.__key() == other.__key()
        return NotImplemented
