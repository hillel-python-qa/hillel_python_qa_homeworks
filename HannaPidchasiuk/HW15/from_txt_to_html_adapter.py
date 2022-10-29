class FromTxtToHtmlAdapter:

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

    def from_txt_to_html(self):
        with open(self.__file_path, 'r') as file:
            file_data = file.readlines()

        tags = file_data[0].replace('\n', '').split(',')
        users = [user.replace('\n', '').split(',') for user in file_data[1:]]
        result = []

        for user in users:
            for index in range(len(tags)):
                result.append(self.__create_tag(tags[index], user[index]))
        return result

    @staticmethod
    def __create_tag(tag_name, value):
        return f'<{tag_name}>{value}</{tag_name}>\n'


if __name__ == '__main__':
    test = FromTxtToHtmlAdapter("test.txt")
    print(test.from_txt_to_html())
