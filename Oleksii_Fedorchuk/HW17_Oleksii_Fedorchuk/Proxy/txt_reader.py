from Project_Git.hillel_python_qa_homeworks.Oleksii_Fedorchuk.HW17_Oleksii_Fedorchuk.Proxy.reader import Reader


class TxtReader(Reader):
    def __init__(self, file_path):
        self.__file_path = f"{file_path}.txt"

    def read(self):
        with open(self.__file_path, "r") as file:
            text = file.read()
            return text
