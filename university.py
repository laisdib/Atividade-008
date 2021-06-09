import department


class University:
    def __init__(self, name):
        self.department_list = []
        self.name = name

    def insert_department(self, name):
        self.department_list.append(department.Department(name))

    def __str__(self):
        return "%s [%s]" % (self.name, \
            ", ".join([item.name for item in self.department_list]))
