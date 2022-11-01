from abc import ABC
from Project_Git.hillel_python_qa_homeworks.Oleksii_Fedorchuk.HW17_Oleksii_Fedorchuk.Proxy.writer import Writer


class TxtWriter(Writer, ABC):
    def __init__(self, file_path):
        self.__file_path = f"{file_path}.txt"

    def write(self, new_data):
        with open(self.__file_path, "w") as file:
            text = file.write(new_data)
            return text
