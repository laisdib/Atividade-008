class Subject:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.teachers_list = []

    def add_teacher(self, teacher):
        self.teachers_list.append(teacher)

    def __str__(self):
        return "%s %s [%s]" % (self.name, self.code, \
            ", ".join([teacher.name for teacher in self.teachers_list]))