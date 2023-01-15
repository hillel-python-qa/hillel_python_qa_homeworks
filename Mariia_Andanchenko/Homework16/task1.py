# Create an iterator that accepts a sequence and can iterate over values with a given range.
# CustomIterator(sequence, start_index, end_index)

class CustomIterator:

    def __init__(self, sequence: list, start_index: int, end_index: int):
        self.__sequence = sequence
        if start_index >= end_index:
            raise ValueError("Start index can't be bigger/equal to end index.")
        if end_index <= start_index:
            raise ValueError("End index can't be less/equal to than start index.")
        if end_index > len(sequence) - 1:
            raise ValueError("End index can't be bigger than len of the list.")

        self.__end_index = end_index
        self.__start_index = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index < self.__end_index:
            item = self.__sequence[self.__start_index]
            self.__start_index += 1
            return item
        else:
            raise StopIteration


if __name__ == '__main__':
    test_list = [1, 4, 4, 4, 7, 4]
    custom_iter = CustomIterator(test_list, 0, 5)
    for test_item in custom_iter:
        print(test_item)
