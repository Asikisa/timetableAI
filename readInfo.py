from Student import Student
from Audience import Audience
from Teacher import Teacher
from Subject import Subject
from Speciality import Speciality
import chromosome

students = []
with open('data/students.txt') as st_file:
    for st_line in st_file:
        line = st_line.strip().split('#')
        name = line[0]
        speciality = line[1]
        group = line[len(line) - 1]
        subjects = line[2:len(line) - 1]
        students.append(Student(name, speciality, subjects, group))

specialities = []
with open('data/specialties.txt') as sp_file:
    for sp_line in sp_file:
        name = sp_line.strip()
        number = 0
        for s in students:
            if s.speciality == name:
                number += 1
        specialities.append(Speciality(name, number))

audiences = []
a_num = 1
with open('data/audiences.txt') as a_file:
    for a_line in a_file:
        audiences.append(Audience(a_num, a_line.strip()))
        a_num += 1

subjects = []
with open('data/subjects.txt') as su_file:
    for su_line in su_file:
        name = su_line.strip()
        enrolled_students_1 = []
        enrolled_students_2 = []
        for s in students:
            for s_sub in s.subjects:
                if s_sub == name:
                    if int(s.group) == 1:
                        enrolled_students_1.append(s)
                    else:
                        enrolled_students_2.append(s)
        subject = Subject(name, enrolled_students_1, enrolled_students_2)
        subjects.append(subject)

teachers = []
with open('data/teachers.txt') as t_file:
    for t_line in t_file:
        t_line = t_line.strip().split('#')
        name = t_line[0]
        subject = t_line[1:]
        teachers.append(Teacher(name, subjects))

# print(chromosome.evolution(teachers, audiences, subjects, specialities))
# best_appearance, num = chromosome.evolution(teachers, audiences, subjects, specialities)
# print(f"Number of generations: {num}, best: {best_appearance.appearance}")
