from automation.hillel_python_qa_homeworks.Andrii_Voinenko.Lesson17.writer_proxy.txt_reader import TxtReader
from automation.hillel_python_qa_homeworks.Andrii_Voinenko.Lesson17.writer_proxy.txt_writer import TxtWriter


class TxtProxyWriterReader:
    def __init__(self, txt_action):
        self.__result = ''
        self.__is_actual = False
        self.__txt_action = txt_action

    def update_actual_status(self, actual_status: bool):
        self.__is_actual = actual_status

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__txt_action.read()
            self.__is_actual = True
            return self.__result

    def write_file(self, file_path: str, new_data):
        self.__result = TxtWriter(file_path).write(new_data)
        self.__is_actual = False
        return self.__result


if __name__ == '__main__':
    txt_reader = TxtReader('test_file.txt')
    proxy_reader = TxtProxyWriterReader(txt_reader)

    print(proxy_reader.read_file())
    print('\n')
    print(proxy_reader.read_file())
    print('\n')
    print(proxy_reader.write_file('test_file.txt', 'Additional text'))
    print('\n')
    print(proxy_reader.read_file())
