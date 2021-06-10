from department import Department


class University:
    def __init__(self, name):
        self.department_list = set()
        self.name = name

    def insert_department(self, name, teacher_list):
        self.department_list.add(Department(name, teacher_list))

    def __str__(self):
        return "%s" % self.name
