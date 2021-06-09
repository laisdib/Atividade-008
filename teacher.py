class Teacher:

    teacher_name = ""
    teacher_code = 0  # Número de 3 dígitos
    subjects_list = []

    def __init__(self, name, code):
        self.teacher_name = name
        self.teacher_code = code

    def output_teacher(self):
        print(self.teacher_name, "%03d" % self.teacher_code, self.subjects_list)

    def add_subject(self, subject):
        self.subjects_list.append(subject)

    def __str__(self):
        return "%s %d" % (self.teacher_name, self.teacher_code)
