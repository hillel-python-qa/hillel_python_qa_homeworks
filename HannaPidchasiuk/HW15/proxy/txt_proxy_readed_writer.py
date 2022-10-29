from HannaPidchasiuk.HW15.proxy.txt_reader import TxtReader
from HannaPidchasiuk.HW15.proxy.txt_writer import TxtWriter


class TxtProxyWriterReader:
    __PASS_KEY = '12345'

    def __init__(self, file_path: str):
        self.__result = ''
        self.__is_actual = False
        self.__txt_reader = TxtReader(file_path)
        self.__txt_writer = TxtWriter(file_path)

    def read_file(self) -> str:
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__txt_reader.read()
            self.__is_actual = True
            return self.__result

    def write_file(self, new_data: str, password: str) -> None:
        if password == TxtProxyWriterReader.__PASS_KEY:
            self.__txt_writer.write(new_data)
        else:
            print("You are not allowed to write!")


if __name__ == '__main__':
    proxy_writer = TxtProxyWriterReader('test_proxy.txt')
    test_data = [23, 34, 432, "slkdj", (34, 55)]
    proxy_writer.write_file(str(test_data), "12345")
    proxy_writer.write_file(str(test_data), "1245")
