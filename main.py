# Exercise 008: Class Diagram

import subject
import teacher


def main():
    teachers_names = ["Jucimar", "Elloá", "Edgar", "Sílvia Cristina", "Márcia"]
    teachers_list = []

    for i in range(5):
        teachers_list.append(teacher.Teacher(teachers_names[i], i + 1))

    subjects_names = ["MD", "Cálculo I", "OAC", "PCA", "LPC I"]
    subjects_list = []

    for i in range(5):
        # Formatting the code to SB001, SB002, SB003, ...
        subjects_list.append(subject.Subject(subjects_names[i], "SB%03d" % (i + 1)))

    for i in range(5):
        teachers_list[i].add_subject(subjects_list[i])
        subjects_list[i].add_teacher(teachers_list[i])

    print("TEACHERS:")
    for i in range(5):
        teachers_list[i].output_teacher()

    print("\nSUBJECTS:")
    for i in range(5):
        subjects_list[i].output_subject()


main()
