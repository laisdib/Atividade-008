class Subject:

    subject_name = ""
    subject_code = ""  # Números e Letras com 5 dígitos
    teachers_list = []

    def __init__(self, name, code):
        self.subject_name = name
        self.subject_code = code

    def output_subject(self):
        print(self.subject_name, self.subject_code, self.teachers_list)

    def add_teacher(self, teacher):
        self.teachers_list.append(teacher)

    def __str__(self):
        return "%s %s" % (self.subject_name, self.subject_code)