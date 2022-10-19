from hillel_python_qa_homeworks.Olha_Lesiuk.HW_15.task_2.reader import Reader


class TxtReader(Reader):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as file:
            text = file.read()
            return text
