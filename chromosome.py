import random
import readInfo
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
    correct_set = set(readInfo.subjects)
    result_set = set()
    for week in x.appearance.weeks:
        for day in week.days:
            for lesson in day.lessons:
                result_set.add(lesson)
    return result_set == correct_set


def check_teacher(x, lesson):
    result = False
    type_of_lesson = lesson.type_of_lesson
    teacher = lesson.teacher
    subject = lesson.subject
    if type_of_lesson == 'lecture':
        if subject not in teacher.subjects:
            result = True
    return result


def match(x):
    output = 0

    for speciality in range(len(x.appearance.weeks)):
        for day in range(len(day_of_week)):
            for lesson in x.appearance.get_lessons_of_day_of_speciality(speciality, day):
                if check_is_busy_teacher(x, lesson, day):
                    output += 1
                if check_is_busy_student(x, lesson, day):
                    output += 1
                if check_teacher(x, lesson):
                    output += 1
                if check_audience(lesson):
                    output += 1
                if check_has_all_lessons(x):
                    output += len(readInfo.subjects)

    return output


def select(offsprings, survivals_size):
    survivals = list(map(lambda x: (match(x), x), offsprings))
    survivals = sorted(survivals, key=lambda x: x[0])

    return list(map(lambda x: x[1], survivals[:survivals_size]))


def random_timetable(teachers, audiences, subjects, specialities):
    current_timetable = []
    for speciality in specialities:
        days_in_week = []
        for day in day_of_week:
            lessons_in_day = []
            num_of_lessons = random.choice(range(1, 7))
            for numb in range(num_of_lessons):
                num_of_lesson = random.choice(range(1, 7))
                type_of_lesson = random.choice(l_or_p)
                subject = random.choice(subjects)
                teacher = random.choice(teachers)
                audience = random.choice(audiences)
                if type_of_lesson == 'practice':
                    group = random.choice([1, 2])
                    lesson = Lesson(num_of_lesson, type_of_lesson, subject, teacher, audience, group)
                else:
                    lesson = Lesson(num_of_lesson, type_of_lesson, subject, teacher, audience)
                lessons_in_day.append(lesson)
            current_day = Day(day, lessons_in_day)
            days_in_week.append(current_day)
        current_week = Week(speciality, days_in_week)
        current_timetable.append(current_week)
    timetable = Timetable(current_timetable)
    return timetable


def mutate(member, teachers, audiences, subjects, specialities):
    input_str = member.appearance
    genes = member.genes
    genes.append(input_str)

    rand_speciality = random.choice(range(len(specialities)))
    rand_day_of_week = random.choice(range(len(day_of_week)))
    range_for_rand = range(member.appearance.get_num_of_lessons_of_day_of_speciality(rand_speciality, rand_day_of_week))
    if range_for_rand:
        rand_n_lesson = random.choice(range_for_rand)

        rand_param = random.choice(parameter)
        if rand_param == 'num_of_lesson':
            new_param = random.choice(range(1, 7))
            member.appearance.set_num_of_lesson_of_day_of_speciality(rand_speciality, rand_day_of_week, rand_n_lesson,
                                                                     new_param)
        elif rand_param == 'type_of_lesson':
            new_param = random.choice(l_or_p)
            member.appearance.set_type_of_lesson_of_day_of_speciality(rand_speciality, rand_day_of_week, rand_n_lesson,
                                                                      new_param)
        elif rand_param == 'subject':
            new_param = random.choice(subjects)
            member.appearance.set_subject_of_lesson_of_day_of_speciality(rand_speciality, rand_day_of_week,
                                                                         rand_n_lesson,
                                                                         new_param)
        elif rand_param == 'teacher':
            new_param = random.choice(teachers)
            member.appearance.set_teacher_of_lesson_of_day_of_speciality(rand_speciality, rand_day_of_week,
                                                                         rand_n_lesson,
                                                                         new_param)
        elif rand_param == 'audience':
            new_param = random.choice(audiences)
            member.appearance.set_audience_of_lesson_of_day_of_speciality(rand_speciality, rand_day_of_week,
                                                                          rand_n_lesson,
                                                                          new_param)

        # elif rand_param == 'add_lesson':
        #     numoflesson = random.choice(range(1, 4))
        #     typeoflesson = random.choice(l_or_p)
        #     subject = random.choice(subjects)
        #     teacher = random.choice(teachers)
        #     audience = random.choice(audiences)
        #     new_param = Lesson(numoflesson, typeoflesson, subject, teacher, audience)
        #     member.appearance.add_lesson_of_day_of_speciality(rand_speciality, rand_day_of_week, new_param)

        # elif rand_param == 'remove_lesson':
        #     random_for_new_param = member.appearance.get_lessons_of_day_of_speciality(rand_speciality, rand_day_of_week)
        #     if random_for_new_param:
        #         new_param = random.choice(random_for_new_param)
        #         member.appearance.remove_lesson_of_day_of_speciality(rand_speciality, rand_day_of_week, new_param)
    return member


def reproduce(member, offsprings_size, teachers, audiences, subjects, specialities):
    output = []

    for i in range(offsprings_size):
        output.append(mutate(member, teachers, audiences, subjects, specialities))

    return output


def next_generation(generation, offsprings_size, survivals_size, teachers, audiences, subjects, specialities):
    offsprings = []

    for member in generation:
        offsprings += reproduce(member, offsprings_size, teachers, audiences, subjects, specialities)

    return select(offsprings, survivals_size)


def is_present(generation):
    result = False
    for e in generation:
        if match(e) == 0:
            result = True
    return result


def evolution(teachers, audiences, subjects, specialities, epochs_num=1000):
    rand_timetable = random_timetable(teachers, audiences, subjects, specialities)

    root = Chromosome(rand_timetable, [])
    generation = [root]

    offsprings_size = 20
    survivals_size = 8

    gen_number = 1
    while True:
        # appearance = [chromosome.appearance for chromosome in generation]
        survivals = list(map(lambda x: (match(x), x), generation))
        survivals = sorted(survivals, key=lambda x: x[0])
        print(f"Generation #{gen_number}\n\nMembers: {survivals}")
        print("\n\n-----------------------------------------------------\n\n")
        generation = next_generation(generation, offsprings_size, survivals_size, teachers, audiences,
                                     subjects, specialities)

        if is_present(generation):
            break

        gen_number += 1

        if gen_number > epochs_num:
            break

    return generation[0], gen_number
