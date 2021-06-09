
class Subject:

    subject_name = ""
    subject_code = ""  # Números e Letras com 5 dígitos

    def __init__(self, name, code):
        self.subject_name = name
        self.subject_code = code

    def output_subject(self):
        print(self.subject_name, self.subject_code)
