class Week:
    def __init__(self, speciality, days):
        self.speciality = speciality
        self.days = days

    def __repr__(self):
        result = f'{self.speciality}'
        for day in self.days:
            result += f'{day.day_of_week}'
            for lesson in day.lessons:
                if lesson.type_of_lesson == 'lecture':
                    result += f'\n{lesson.num_of_lesson} {lesson.subject} {lesson.type_of_lesson} {lesson.teacher} {lesson.audience}'
                else:
                    result += f'\n{lesson.num_of_lesson} {lesson.subject} {lesson.num_of_group} {lesson.teacher} {lesson.audience}'
        return result

    def get_students_of_lesson_of_day(self, n_day, n_lesson):
        return self.days[n_day].get_students_of_lesson(n_lesson)

    def get_teacher_of_lesson_of_day(self, n_day, n_lesson):
        return self.days[n_day].get_teacher_of_lesson(n_lesson)

    def get_speciality_of_week(self):
        return self.speciality

    def get_lessons_of_day(self, n_day):
        return self.days[n_day].get_lessons()

    def get_num_of_lessons_of_day(self, n_day):
        return self.days[n_day].get_num_of_lessons()

    def get_num_of_lesson_of_day(self, n_day, n_lesson):
        return self.days[n_day].get_num_of_lesson(n_lesson)

    def get_type_of_lesson_of_day(self, n_day, n_lesson):
        return self.days[n_day].get_type_of_lesson(n_lesson)

    def get_subject_of_lesson_of_day(self, n_day, n_lesson):
        return self.days[n_day].get_subject_of_lesson(n_lesson)

    def get_audience_of_lesson_of_day(self, n_day, n_lesson):
        return self.days[n_day].get_audience_of_lesson(n_lesson)

    def set_num_of_lesson_of_day(self, n_day, n_lesson, arg):
        self.days[n_day].set_num_of_lesson(n_lesson, arg)

    def set_type_of_lesson_of_day(self, n_day, n_lesson, arg):
        self.days[n_day].set_type_of_lesson(n_lesson, arg)

    def set_subject_of_lesson_of_day(self, n_day, n_lesson, arg):
        self.days[n_day].set_subject_of_lesson(n_lesson, arg)

    def set_teacher_of_lesson_of_day(self, n_day, n_lesson, arg):
        self.days[n_day].set_teacher_of_lesson(n_lesson, arg)

    def set_audience_of_lesson_of_day(self, n_day, n_lesson, arg):
        self.days[n_day].set_audience_of_lesson(n_lesson, arg)

    def add_lesson_of_day(self, n_day, arg):
        self.days[n_day].add_lesson(arg)

    def remove_lesson_of_day(self, n_day, arg):
        self.days[n_day].remove_lesson(arg)
