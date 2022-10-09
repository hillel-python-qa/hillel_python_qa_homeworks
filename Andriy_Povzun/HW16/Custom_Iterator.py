class CustomIterator:
    def __init__(self, sequence: list, start_index: int, end_index: int):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index > self.__end_index:
            raise Exception('start index cannot be more than end index')
        if self.__start_index < 0:
            raise Exception('start index cannot be less than 0')
        if self.__end_index > len(self.__sequence):
            self.__end_index = len(self.__sequence)
        if self.__start_index > len(self.__sequence):
            raise Exception('start index out of range')

        if self.__start_index < self.__end_index:
            item = self.__sequence[self.__start_index]
            self.__start_index += 1
            return item
        else:
            raise StopIteration


if __name__ == '__main__':
    test_list = [13, 21, 25, 123, 3124, 124, 222, 151, 21, 412, 4]
    test = CustomIterator(test_list, 0, 100)
    for element in test:
        print(element)
