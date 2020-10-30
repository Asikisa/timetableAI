class Day:
    def __init__(self, day_of_week, lessons):
        self.day_of_week = day_of_week
        self.lessons = lessons

    def __repr__(self):
        result = str(self.day_of_week)
        for lesson in self.lessons:
            if lesson.type_of_lesson == 'lecture':
                result += f'\n {lesson.num_of_lesson} {lesson.subject} {lesson.type_of_lesson} {lesson.teacher} {lesson.audience} '
            else:
                result += f'\n {lesson.num_of_lesson} {lesson.subject} {lesson.num_of_group} {lesson.teacher} {lesson.audience} '
        return result

    def get_students_of_lesson(self, n_lesson):
        for lesson in self.lessons:
            if lesson.num_of_lesson == n_lesson and lesson.type_of_lesson == 'lecture':
                return lesson.subject.enrolled_students_first_group + lesson.subject.enrolled_students_second_group
            elif lesson.num_of_lesson == n_lesson and int(lesson.num_of_group) == 1:
                return lesson.subject.enrolled_students_first_group
            elif lesson.num_of_lesson == n_lesson and int(lesson.num_of_group) == 2:
                return lesson.subject.enrolled_students_second_group
        return []

    def get_teacher_of_lesson(self, n_lesson):
        for lesson in self.lessons:
            if lesson.num_of_lesson == n_lesson:
                return lesson.teacher

    def get_lessons(self):
        return self.lessons

    def get_num_of_lessons(self):
        return len(self.lessons)

    def get_num_of_lesson(self, n_lesson):
        return self.lessons[n_lesson].num_of_lesson

    def get_type_of_lesson(self, n_lesson):
        return self.lessons[n_lesson].type_of_lesson

    def get_subject_of_lesson(self, n_lesson):
        return self.lessons[n_lesson].subject

    def get_audience_of_lesson(self, n_lesson):
        return self.lessons[n_lesson].audience

    def set_num_of_lesson(self, n_lesson, arg):
        self.lessons[n_lesson].num_of_lesson = arg

    def set_type_of_lesson(self, n_lesson, arg):
        self.lessons[n_lesson].type_of_lesson = arg

    def set_subject_of_lesson(self, n_lesson, arg):
        self.lessons[n_lesson].subject = arg

    def set_teacher_of_lesson(self, n_lesson, arg):
        self.lessons[n_lesson].teacher = arg

    def set_audience_of_lesson(self, n_lesson, arg):
        self.lessons[n_lesson].audience = arg

    def add_lesson(self, arg):
        self.lessons.append(arg)

    def remove_lesson(self, arg):
        self.lessons.remove(arg)
