class FromTxtToHTML:
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def from_txt_to_html(self):
        with open(self.__file_path, "r") as file:
            lines = file.readlines()
        for index, value in enumerate(lines):
            print(list(index, value))


if __name__ == '__main__':
    html_data = FromTxtToHTML('data_file.txt').from_txt_to_html()
