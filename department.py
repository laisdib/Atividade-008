class Department:
    def __init__(self, name, teacher_list):
        self.name = name
        self.teacher_list = teacher_list

    def insert_teachers(self, teacher):
        self.teacher_list.append(teacher)

    def __str__(self):
        return "%s [%s]" % (self.name, \
            ", ".join([teacher.name for teacher in self.teacher_list]))
