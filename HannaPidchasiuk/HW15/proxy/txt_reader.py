from HannaPidchasiuk.HW15.proxy.reader import Reader


class TxtReader(Reader):

    def __init__(self, file_path: str):
        self.__file_path = file_path

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value: str):
        if value:
            self.__file_path = value
        else:
            raise ValueError("File path cannot be empty!")

    def read(self):
        with open(self.__file_path, 'r') as file:
            text = file.read()
        return text
