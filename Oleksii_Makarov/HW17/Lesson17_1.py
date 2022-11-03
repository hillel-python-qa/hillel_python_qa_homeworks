class TextToHtml:
    def __init__(self, file_path):
        self.__file_path = file_path

    def html_adapter(self):
        """
            Takes path to file, filled with proper syntax. Syntax: Header1,Header2,... Body1,Body2,... Reads lines and
            replaces all new lines with empty spaces. Splits everything by commas. Then places them in a format:\n
            <Header1>Body1</Header1>\n<Header2>Body2</Header2>\n...
        """
        with open(self.__file_path) as file:
            read_file = file.readlines()
        tags = read_file[0].replace('\n', '').split(',')
        content = []
        for item in read_file[1:]:
            content.append(item.replace('\n', '').split(','))
        pack = []
        for item in content:
            pack.append(dict(zip(tags, item)))
        result = []
        for package in pack:
            for (key, item) in package.items():
                result.append(''.join(f'<{key}>{item}</{key}>\n'))
        return ''.join(result)


if __name__ == '__main__':
    text = TextToHtml('text.txt')
    print(text.html_adapter())
