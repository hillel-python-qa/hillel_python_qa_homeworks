from hillel_python_qa_homeworks.Olha_Lesiuk.HW_15.task_2.txt_reader import TxtReader
from hillel_python_qa_homeworks.Olha_Lesiuk.HW_15.task_2.txt_writer import TxtWriter


class TxtProxyWriterReader:
    def __init__(self, file_path):
        self.__result = ''
        self.__is_actual = False
        self.__txt_reader = TxtReader(file_path)
        self.__txt_writer = TxtWriter(file_path)

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__txt_reader.read()
            self.__is_actual = True
            return self.__result

    def write_file(self):
        self.__result = self.__txt_writer.write(new_data='Ukraine Victory!')
        self.__is_actual = False
        return self.__result


if __name__ == '__main__':
    txt_proxy_writer_reader = TxtProxyWriterReader('my_file.txt')

    print(txt_proxy_writer_reader.read_file())
    txt_proxy_writer_reader.write_file()
    print(txt_proxy_writer_reader.read_file())
    print(txt_proxy_writer_reader.read_file())
