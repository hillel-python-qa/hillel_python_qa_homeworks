class CustomIterator:
    def __init__(self, sequence: list, start_index: int, end_index: int):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index > self.__end_index:
            print("Please double check your indexes. Your start index is higher thn the end index.")
        if self.__start_index > len(self.__sequence):
            print("Your start index is out of range")


        if self.__start_index < self.__end_index:
            item = self.__sequence[self.__start_index]
            self.__start_index += 1
            return item
        else:
            raise StopIteration


if __name__ == '__main__':
    custom_iterator = CustomIterator([1, 2, 3, 4, 5], -1, )

    for item in custom_iterator:
        print(item)
