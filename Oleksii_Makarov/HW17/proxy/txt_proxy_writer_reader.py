from txt_reader import TxtReader
from txt_writer import TxtWriter


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

    def write_file(self, new_value):
        self.__result = self.__txt_writer.write(new_value)
        self.__is_actual = False
        return self.__result


if __name__ == '__main__':
    proxy_reader = TxtProxyWriterReader('my_file.txt')

    print(proxy_reader.read_file())
    proxy_reader.write_file('One two three')
    print(proxy_reader.read_file())
    proxy_reader.write_file('__aaaff')
    print(proxy_reader.read_file())
