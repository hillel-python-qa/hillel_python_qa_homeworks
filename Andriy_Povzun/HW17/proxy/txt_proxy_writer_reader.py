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

    def write_file(self, new_data):
        if not new_data:
            raise ValueError('New data cannot be empty')
        else:
            self.__result = self.__txt_writer.write(new_data)
            self.__is_actual = False
            return self.__result


if __name__ == '__main__':
    proxy = TxtProxyWriterReader('my_file.txt')

    print(proxy.read_file())
    proxy.write_file('Just test :)')
    print(proxy.read_file())
    print(proxy.read_file())
