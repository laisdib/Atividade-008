
class Teacher:

    teacher_name = ""
    teacher_code = 0 # Número de 3 dígitos

    def __init__(self, name, code):
        self.teacher_name = name
        self.teacher_code = code

    def output_teacher(self):
        print(self.teacher_name, "%03d" % self.teacher_code)
