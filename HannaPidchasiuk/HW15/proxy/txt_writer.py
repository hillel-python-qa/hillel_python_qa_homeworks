from HannaPidchasiuk.HW15.proxy.writer import Writer


class TxtWriter(Writer):

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

    def write(self, new_data):
        if new_data:
            with open(self.__file_path, "w") as file:
                text = file.write(new_data)
        else:
            print("Nothing to write!")
        return text
