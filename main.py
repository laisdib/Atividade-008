# Exercise 008: Class Diagram

import subject
import teacher
import department


def main():
    teachers_names = ["Jucimar", "Elloá", "Edgard", "Sílvia Cristina", "Márcia"]
    department_names = ["EST", "ESA", "ESAT", "ENS", "ESO"]
    teachers_list = []
    department_list = []

    for i in range(5):
        teachers_list.append(teacher.Teacher(teachers_names[i], i + 1))
        department_list.append(department.Department(department_names[i]))
        department_list[i].insert_teachers(teachers_list[i])

    subjects_names = ["LPC", "MD", "OAC", "Cálculo I", "PCA"]
    subjects_list = []

    for i in range(5):
        # Formatting the code to SB001, SB002, SB003, ...
        subjects_list.append(subject.Subject(subjects_names[i], "SB%03d" % (i + 1)))

    for i in range(5):
        teachers_list[i].add_subject(subjects_list[i])
        subjects_list[i].add_teacher(teachers_list[i])


    print("TEACHERS:")
    for i in range(5):
        print(teachers_list[i])

    print("\nSUBJECTS:")
    for i in range(5):
        print(subjects_list[i])

    print("\nDEPARTMENTS:")
    for i in range(5):
        print(department_list[i])

main()
