class FromTxtToHtml:
    def __init__(self, file_read: str, file_write: str):
        self.__file_read = file_read
        self.__file_write = file_write

    def from_txt_to_html(self):
        with open(self.__file_read, 'r') as file:
            lines = file.readlines()

        tags = lines[0].replace('\n', '').split(',')
        users = [item.replace('\n', '').split(',') for item in lines[1:]]
        result = []

        for user in users:  # get list of user data
            for index in range(len(tags)):  # get index in range of tags 0-3
                result.append(
                    f'<{tags[index]}>{user[index]}</{tags[index]}>\n')  # due to index get correct user data and tag

        with open(self.__file_write, 'w') as file:
            for item in result:
                file.write(item)  # write all created strings into new file

        return f'Final result could be checked in {self.__file_write}'


if __name__ == '__main__':
    test = FromTxtToHtml('text.txt', 'body.html').from_txt_to_html()
    print(test)
