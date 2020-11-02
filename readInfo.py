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
        group = line[-1]
        subjects = line[2:-1]
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


teachers = []
with open('data/teachers.txt') as t_file:
    for t_line in t_file:
        t_line = t_line.strip().split('#')
        name = t_line[0]
        subjs = t_line[1:]
        teachers.append(Teacher(name, subjs))
        print(name, subjs[0])


subjects = []
with open('data/subjects.txt') as su_file:
    for su_line in su_file:
        s_name = su_line.strip()
        enrolled_students = []
        s_type = ""
        s_teacher = None
        # for s in students:
        #     for s_sub in s.subjects:
        #         if s_sub == name:
        #             enrolled_students.append(s)
        # subject = Subject(name, enrolled_students)
        # subjects.append(subject)
        for t in teachers:
            for subj in t.subjects:
                try:
                    subject, subject_type = subj.split("\\")
                except ValueError:
                    subject = subj
                    subject_type = "lecture"
                if subject == s_name:
                    s_teacher = t
                    s_type = subject_type
                    if subject_type == "lecture":
                        for student in students:
                            if s_name in student.subject_names:
                                enrolled_students.append(student)
                    else:
                        s_group = subject_type[-1]
                        for student in students:
                            if s_name in student.subject_names and student.group == s_group:
                                enrolled_students.append(student)
        if s_type == "" or s_teacher is None:
            raise Exception("no teachers found for this subject")
        subjects.append(Subject(s_name, s_type, enrolled_students, s_teacher))


# print(chromosome.evolution(teachers, audiences, subjects, specialities))
# best_appearance, num = chromosome.evolution(teachers, audiences, subjects, specialities)
# print(f"Number of generations: {num}, best: {best_appearance.appearance}")
