class CustomIterator:
    def __init__(self, sequence: list, start_index: int, end_index: int):
        self.__sequence = sequence
        # start index accepts both positive and negative values
        self.__start_index = start_index
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__end_index < self.__start_index:
            raise ValueError("Invalid value! The end index shouldn't be lower than a start index!")

        if self.__start_index < len(self.__sequence):
            item = self.__sequence[self.__start_index]
            self.__start_index += 1
            return item
        else:
            raise StopIteration


if __name__ == "__main__":
    custom_iterator = CustomIterator([555, 91, 99, -99, 1000, 65, 101], -5, 1000)
    iterator = iter(custom_iterator)

    for i in custom_iterator:
        print(i)
