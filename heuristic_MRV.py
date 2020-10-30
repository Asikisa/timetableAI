import random
import readInfo as rf
from Lesson import Lesson
from Day import Day
from Week import Week
from Timetable import Timetable

day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
l_or_p = ['lecture', 'practice']
parameter = ['num_of_lesson', 'type_of_lesson', 'subject', 'teacher', 'audience']


class Chromosome:
    def __init__(self, appearance, genes):
        self.appearance = appearance
        self.genes = genes

    def __repr__(self):
        return f'{self.appearance}'


def check_audience(lesson):
    result = False
    # BEFORE
    # if lesson.type_of_lesson == 'lecture' and lesson.audience.capacity < lesson.subject.get_num_of_students():
    if lesson.type_of_lesson == 'lecture' and lesson.audience.capacity >= lesson.subject.get_num_of_students():
        result = True
    # elif lesson.type_of_lesson == 'practice' and lesson.num_of_group == 1 and lesson.audience.capacity \
    #         < len(lesson.subject.enrolled_students_first_group):
    elif lesson.type_of_lesson == 'practice' and lesson.num_of_group == 1 and lesson.audience.capacity \
            >= len(lesson.subject.enrolled_students_first_group):
        result = True

    # elif lesson.type_of_lesson == 'practice' and lesson.num_of_group == 2 and lesson.audience.capacity \
    #         < len(lesson.subject.enrolled_students_second_group):
    elif lesson.type_of_lesson == 'practice' and lesson.num_of_group == 2 and lesson.audience.capacity \
            >= len(lesson.subject.enrolled_students_second_group):
        result = True
    return result


def check_is_busy_teacher(x, lesson, day):
    result = False
    n_lesson = lesson.num_of_lesson
    busy_teachers = x.appearance.get_teachers_of_lesson(day, n_lesson)
    for teacher in busy_teachers:
        if busy_teachers.get(teacher) >= 1:
            result = True
    return result


def check_is_busy_student(x, lesson, day):
    result = False  # ADD THIS
    busy_students = x.appearance.get_students_of_lesson(day, lesson)
    for student in busy_students:
        if busy_students.get(student) >= 1:
            result = True
    return result


def check_has_all_lessons(x):
    correct_set = set(rf.subjects)
    result_set = set()
    for week in x.appearance.weeks:
        for day in week.days:
            for lesson in day.lessons:
                result_set.add(lesson)
    return result_set == correct_set


def check_teacher(lesson):
    result = False
    type_of_lesson = lesson.type_of_lesson
    teacher = lesson.teacher
    subject = lesson.subject
    if type_of_lesson == 'lecture':
        if subject not in teacher.subjects:
            result = True
    return result

# --------------------------------------------------


# subjects_restrictions = {"discretka":{"lecture":[laag], "practice_1":[matan], "practice_2":[teorver, ...]}}
subjects_restrictions = dict.fromkeys(rf.subjects, dict.fromkeys(["lecture", "practice_1", "practice_2"], []))
subjects_domens = dict.fromkeys(rf.subjects, [])

subj_restr = dict.fromkeys(rf.subjects)

def all_restrictions():
    for subject in subjects_restrictions.keys():
        for subj2 in rf.subjects:
            if subj2 is subject:
                break
            for student in subject.enrolled_students_first_group:
                if student in subj2.enrolled_students_first_group:
                    subjects_restrictions[subject]["practice_1"].append(subj2.name)
                    subjects_restrictions[subject]["lecture"].append(subj2.name)
                    break
                if student in subj2.enrolled_students_second_group:
                    subjects_restrictions[subject]["practice_2"].append(subj2.name)
                    subjects_restrictions[subject]["lecture"].append(subj2.name)
                    break








