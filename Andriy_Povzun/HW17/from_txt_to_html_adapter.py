class FromTxtToHtmlAdapter:
    def __init__(self, file_path):
        self.__file_path = file_path

    def from_txt_to_html(self):
        with open(self.__file_path, 'r') as file:
            rows = file.readlines()
            headers = rows[0].replace('\n', '').split(',')
            data = [row.replace('\n', '').split(',') for row in rows[1:]]
            result = []
            for y in range(0, len(data)):
                i = 0
                while i < len(headers):
                    if i == 0:
                        result.append('<user_data>\n')
                    result.append(f'\t<{headers[i]}>{data[y][i]}</{headers[i]}>\n')
                    if i == len(headers) - 1:
                        result.append('</user_data>\n')
                    i += 1
                y += 1
            html = '\n'.join(result)
            return html


if __name__ == '__main__':
    my_html = FromTxtToHtmlAdapter('Users.txt').from_txt_to_html()
    print(my_html)
