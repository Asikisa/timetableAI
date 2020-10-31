import random
import readInfo as rf
from Lesson import Lesson, EmptyLesson

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# l_or_p = ['lecture', 'practice']
parameter = ['num_of_lesson', 'type_of_lesson', 'subject', 'teacher', 'audience']


# class Chromosome:
#     def __init__(self, appearance, genes):
#         self.appearance = appearance
#         self.genes = genes
#
#     def __repr__(self):
#         return f'{self.appearance}'


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


subjects_domens = dict.fromkeys(rf.subjects, [])
subj_restrictions = dict.fromkeys(rf.subjects)
week = [EmptyLesson(day, lesson) for day in days_of_week for lesson in range(6)]


def build_restrictions_table():
    # for subject in subjects_restrictions.keys():
    for subject in subj_restrictions:
        counter = 0
        for subj2 in rf.subjects:
            if subj2 is subject:
                break
            elif subject.name == subj2.name:
                if subject.subj_type == "lecture" or subj2.subj_type == "lecture":
                    counter += 1
                    break
            if subject.teacher == subj2.teacher:
                counter += 1
                break
            for student in subject.enrolled_students:
                if student in subj2.enrolled_students:
                    # subjects_restrictions[subject]["practice_1"].append(subj2.name)
                    counter += 1
                    break
##########


def build_domens():
    for subject in subjects_domens:
        subjects_domens[subject] = week


#########


#
def mrv():
    x = 1000
    min_s = None
    for s, i in subjects_domens.items():
        if 0 < len(i) < x:
            min_s = s
            x = len(i)
    return min_s


#########


# least constraining value - choosing a value for next variable
def lcv_heuristic():
    a = dict.fromkeys(week)
    for empty_l in week:
        counter = 0
        for subj in subjects_domens:
            if empty_l in subj:
                counter += 1
        a[empty_l] = counter
    return dict_max(a)


#####


# choosing the very first variable to choose a value
def degree_heuristic():
    current_subj = dict_max(subj_restrictions)
    return current_subj


# ####????


def dict_max(dic):
    dic_list = dic.items()
    max_el = dic_list[0]
    for i in dic_list[1:]:
        if type(max_el[1]) is not type(i[1]):
            raise Exception("not comparable types of values")
        if i[1] > max_el[1]:
            max_el = i
    return max_el[0]
