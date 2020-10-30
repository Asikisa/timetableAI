class Timetable:
    def __init__(self, weeks):
        self.weeks = weeks

    def __repr__(self):
        result = ''
        for week in self.weeks:
            result += '\n Speciality: ' + week.speciality.name + '\n'
            for day in week.days:
                result += '\n' + day.day_of_week
                for lesson in day.lessons:
                    if lesson.type_of_lesson == 'lecture':
                        result += f'\n{lesson.num_of_lesson} lesson, {lesson.subject}, {lesson.type_of_lesson}, teacher: {lesson.teacher}, audience room: {lesson.audience} '
                    else:
                        result += f'\n{lesson.num_of_lesson} lesson, {lesson.subject}, {lesson.num_of_group} practice group, teacher: {lesson.teacher}, audience room: {lesson.audience}'
        return result

    def get_students_of_lesson(self, n_day, n_lesson):
        result = {}
        for speciality in range(len(self.weeks)):
            students = self.weeks[speciality].get_students_of_lesson_of_day(n_day, n_lesson)
            for s in students:
                if s in result:
                    num = result.get(s)
                    num += 1
                    result[s] = num
                else:
                    result[s] = 1
        return result

    def get_teachers_of_lesson(self, n_day, n_lesson):
        result = {}
        for speciality in range(len(self.weeks)):
            teacher = self.weeks[speciality].get_teacher_of_lesson_of_day(n_day, n_lesson)
            if teacher in result:
                num = result.get(teacher)
                num += 1
                result[teacher] = num
            else:
                result[teacher] = 1
        return result

    def get_specialities(self):
        result = ''
        for week in range(len(self.weeks)):
            result += f'#{self.weeks[week].get_speciality_of_week}'
        return result

    def get_lessons_of_day_of_speciality(self, n_week, n_day):
        return self.weeks[n_week].get_lessons_of_day(n_day)

    def get_num_of_lessons_of_day_of_speciality(self, n_week, n_day):
        return self.weeks[n_week].get_num_of_lessons_of_day(n_day)

    def add_lesson_of_day_of_speciality(self, n_week, n_day, arg):
        self.weeks[n_week].add_lesson_of_day(n_day, arg)

    def remove_lesson_of_day_of_speciality(self, n_week, n_day, arg):
        self.weeks[n_week].remove_lesson_of_day(n_day, arg)

    def get_num_of_lesson_of_day_of_speciality(self, n_week, n_day, n_lesson):
        return self.weeks[n_week].get_num_of_lesson_of_day(n_day, n_lesson)

    def get_type_of_lesson_of_day_of_speciality(self, n_week, n_day, n_lesson):
        return self.weeks[n_week].get_type_of_lesson_of_day(n_day, n_lesson)

    def get_subject_of_lesson_of_day_of_speciality(self, n_week, n_day, n_lesson):
        return self.weeks[n_week].get_subject_of_lesson_of_day(n_day, n_lesson)

    def get_teacher_of_lesson_of_day_of_speciality(self, n_week, n_day, n_lesson):
        return self.weeks[n_week].get_teacher_of_lesson_of_day(n_day, n_lesson)

    def get_audience_of_lesson_of_day_of_speciality(self, n_week, n_day, n_lesson):
        return self.weeks[n_week].get_audience_of_lesson_of_day(n_day, n_lesson)

    def set_num_of_lesson_of_day_of_speciality(self, n_week, n_day, n_lesson, arg):
        self.weeks[n_week].set_num_of_lesson_of_day(n_day, n_lesson, arg)

    def set_type_of_lesson_of_day_of_speciality(self, n_week, n_day, n_lesson, arg):
        self.weeks[n_week].set_type_of_lesson_of_day(n_day, n_lesson, arg)

    def set_subject_of_lesson_of_day_of_speciality(self, n_week, n_day, n_lesson, arg):
        self.weeks[n_week].set_subject_of_lesson_of_day(n_day, n_lesson, arg)

    def set_teacher_of_lesson_of_day_of_speciality(self, n_week, n_day, n_lesson, arg):
        self.weeks[n_week].set_teacher_of_lesson_of_day(n_day, n_lesson, arg)

    def set_audience_of_lesson_of_day_of_speciality(self, n_week, n_day, n_lesson, arg):
        self.weeks[n_week].set_audience_of_lesson_of_day(n_day, n_lesson, arg)
