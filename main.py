# Exercise 008: Class Diagram

import subject
import teacher
import university


def main():
    teachers_names = ["Jucimar", "Elloá", "Edgard", "Sílvia Cristina", "Márcia"]
    teachers_list = []
    departments_teacher_list = []

    for i in range(5):
        # Teacher code is 0, 1, 2, ...
        teachers_list.append(teacher.Teacher(teachers_names[i], i + 1))
        departments_teacher_list.append(teachers_list[i])
    
    subjects_names = ["LPC", "MD", "OAC", "Cálculo I", "PCA"]
    subjects_list = []

    for i in range(5):
        # Subject code is SB001, SB002, SB003, ...
        subjects_list.append(subject.Subject(subjects_names[i], "SB%03d" % (i + 1)))

    for i in range(5):
        teachers_list[i].add_subject(subjects_list[i])
        subjects_list[i].add_teacher(teachers_list[i])

    department_names = ["EST", "ESA", "ESAT", "ENS", "ESO"]
    university_object = university.University("Universidade do Estado do Amazonas")

    for i in range(5):
        university_object.insert_department(department_names[i], teachers_list[i])

    print("\nUNIVERSITY")
    print(university_object)
    print("[", end="")

    flag = 0
    for department_item in university_object.department_list:
        if flag == 1:
            print(", ", end="")
        print(department_item.name, end="")
        flag = 1
    print("]")

    flag = 0
    print('\nDEPARTMENTS:')
    for department_item in university_object.department_list:
        print(department_item.name, "[" + departments_teacher_list[flag].name, "%03d" % departments_teacher_list[flag].code + "]")
        flag += 1

    print("\nTEACHERS:")
    for i in range(5):
        print(teachers_list[i])

    print("\nSUBJECTS:")
    for i in range(5):
        print(subjects_list[i])

    print()


main()
