class Teacher:
    def __init__(self, name, code):
        self.subjects_list = []
        self.name = name
        self.code = code

    def add_subject(self, subject):
        self.subjects_list.append(subject)

    def __str__(self):
        return "%s %03d [%s]" % (self.name, self.code, \
            ", ".join([subject.name for subject in self.subjects_list]))
