class FromTxtToHtmlAdapter:
    def __init__(self, file_path):
        self.__file_path = file_path

    def from_txt_to_html(self):
        with open(self.__file_path, 'r') as file:
            rows = file.readlines()
            headers = rows[0].replace('\n', '').split(',')
            data = [row.replace('\n', '').split(',') for row in rows[1:]]
            result = []
            for column in range(0, len(data)):
                index = 0
                while index < len(headers):
                    if index == 0:
                        result.append('<user_data>')
                    result.append(f'<{headers[index]}>{data[column][index]}</{headers[index]}>')
                    if index == len(headers) - 1:
                        result.append('</user_data>')
                    index += 1
                column += 1
            html = '\n'.join(result)
            return html


if __name__ == '__main__':
    my_html = FromTxtToHtmlAdapter('Users.txt').from_txt_to_html()
    print(my_html)
