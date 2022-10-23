from Project_Git.hillel_python_qa_homeworks.Oleksii_Fedorchuk.HW17_Oleksii_Fedorchuk.Proxy.txt_reader import TxtReader
from Project_Git.hillel_python_qa_homeworks.Oleksii_Fedorchuk.HW17_Oleksii_Fedorchuk.Proxy.txt_writer import TxtWriter


class TxtProxyWriterReader:
    def __init__(self, file_path):
        self.__result = ""
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

    def write_file(self, new_data):
        self.__result = self.__txt_writer.write(new_data)
        self.__is_actual = False
        return self.__result


if __name__ == '__main__':
    proxy_reader = TxtProxyWriterReader("my_file")
    print(proxy_reader.read_file())
    proxy_reader.write_file('Test1')
    print(proxy_reader.read_file())
    proxy_reader.write_file('')
    print(proxy_reader.read_file())
    proxy_reader.write_file('Test2')
    print(proxy_reader.read_file())
