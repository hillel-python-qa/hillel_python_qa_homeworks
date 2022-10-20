class FromTxtToHtmlAdapter:
    def __init__(self, file_path):
        self.__file_path = file_path

    def from_txt_to_html(self):
        with open(self.__file_path) as file:
            lines = file.readlines()
            headers = lines[0].replace('\n', '').split(',')

        data = [item.replace('\n', '').split(',') for item in lines[1:]]
        results = []
        for user_data in data:
            results.append(dict(zip(headers, user_data)))
        convert_to_html = []
        for _ in results:
            convert_to_html.append(''.join([f'<{item}>{value}</{item}>\n' for (item, value) in _.items()]))
        return '\n'.join(convert_to_html)


if __name__ == '__main__':
    html = FromTxtToHtmlAdapter('text.txt').from_txt_to_html()
    print(html)
