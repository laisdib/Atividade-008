# Exercise 008: Class Diagram

import subject
import teacher


def main():
     teachers_names = ["Leandro", "Fábio", "Levi", "Gustavo", "Laís"]
     teachers_list = []

     for i in range(5):
          teachers_list.append(teacher.Teacher(teachers_names[i], i + 1))

     subjects_names = ["MD", "Cálculo I", "Álgebra Linear", "PCA", "OAC"]
     subjects_list = []
     
     for i in range(5):
          # Formatting the code to ESTCMP001, ESTCMP002, ESTCMP003, ...
          subjects_list.append(subject.Subject(subjects_names[i], "ESTCMP%03d" % (i + 1)))

     print("TEACHERS:")
     for i in range(5):
          teachers_list[i].output_teacher()

     print("\nSUBJECTS:")
     for i in range(5):
          subjects_list[i].output_subject()


main()
