class CustomIterator:
    def __init__(self, sequence: list, start_index: int, end_index: int):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index > self.__end_index:
            raise IndexError("Start index cannot be more then End index")
        if self.__end_index > len(self.__sequence):
            raise IndexError("Out of range")
        if self.__end_index == self.__start_index:
            raise IndexError("Start index cannot equalize End index ")
        if self.__start_index < self.__end_index:
            item = self.__sequence[self.__start_index]
            self.__start_index += 1
            return item
        else:
            raise StopIteration


if __name__ == '__main__':
    iterator_list = [10, 20, 300, 500, 1, 473]
    itr = CustomIterator(iterator_list, 1, 1)
    for i in itr:
        print(i)
