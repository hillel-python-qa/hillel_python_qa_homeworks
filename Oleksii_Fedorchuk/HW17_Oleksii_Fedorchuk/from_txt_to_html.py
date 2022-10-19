def tag(name, value):
    return f"<{name}>{value}<{name}>"


class FromTxtToHTML:
    def __init__(self, file_path: str):
        self.__file_path = file_path

    @property
    def file_path(self):
        return self.__file_path

    def from_txt_to_html(self):
        with open(self.__file_path, "r") as file:
            lines = file.readlines()
        html_tags = lines[0].replace("\n", "").split(",")
        data = [user.replace("\n", "").split(",") for user in lines[1:]]
        end_result = []
        for user in data:
            for i in range(len(html_tags)):
                end_result.append(tag(html_tags[i], user[i]))
        return print(end_result)


if __name__ == '__main__':
    FromTxtToHTML('data_file.txt').from_txt_to_html()
