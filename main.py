# Exercise 008: Class Diagram

from random import randint
from subject import Subject
from teacher import Teacher
from university import University


def main():
    teachers_names = [
        "Jucimar",
        "Elloá",
        "Edgard",
        "Sílvia",
        "Márcia",
        "Ricardo",
    ]
    teachers_list = []

    for i in range(len(teachers_names)):
        # Teacher code is 001, 002, 003, ...
        teachers_list.append(Teacher(teachers_names[i], randint(1, 999)))

    subjects_names = [
        "LPC",
        "MD",
        "OAC",
        "Cálculo I",
        "PCA",
        "Álgebra Linear",
        "Fundamentos de SI",
    ]
    subjects_list = []

    for i in range(len(subjects_names)):
        # Subject code is SB001, SB002, SB003, ...
        subjects_list.append(
            Subject(subjects_names[i], "SB%03d" % randint(1, 999))
        )

    for i in range(len(teachers_list)):
        # Add j subjects for the teacher in position i
        times = randint(1, len(subjects_list))
        while times:
            position = randint(0, len(subjects_list) - 1)
            teachers_list[i].add_subject(subjects_list[position])
            subjects_list[position].add_teacher(teachers_list[i])
            times -= 1

    department_names = ["EST", "ESA", "ESAT", "ENS", "ESO"]
    university_object = University("Universidade do Estado do Amazonas")

    for i in range(len(department_names)):
        department_teachers = set()
        # Add j teachers for the department in position i
        times = randint(1, len(teachers_list))
        while times:
            department_teachers.add(
                teachers_list[randint(0, len(teachers_list) - 1)]
            )
            times -= 1

        university_object.insert_department(
            department_names[i], department_teachers
        )

    print("\nUNIVERSITY")
    print(university_object, end=" ")
    print("[", end="")

    first = True
    for department_item in university_object.department_list:
        if not first:
            print(", ", end="")
        else:
            first = False
        print(department_item.name, end="")
    print("]")

    print("\nDEPARTMENTS:")
    for department in university_object.department_list:
        print(department)

    print("\nTEACHERS:")
    for i in range(5):
        print(teachers_list[i])

    print("\nSUBJECTS:")
    for i in range(5):
        print(subjects_list[i])

    print()


main()
