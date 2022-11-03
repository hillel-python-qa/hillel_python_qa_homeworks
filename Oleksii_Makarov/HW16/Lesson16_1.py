class MyIterator:
    def __init__(self, iter_object: iter, start_value: int, end_value: int):
        self.__iter_object = iter_object
        self.__start_value = start_value
        self.__end_value = end_value

    def __iter__(self):
        return self

    def __next__(self):
        """
            If end_value and start_value have passed checks, while start_value is less than end_value
            then function returns value of index of list equal to start_value and increments start_value by 1, repeating
            the process until start_value would be equal to end_value.
            Start_value must not be bigger than end_value.
            End_value must not be bigger than length of iterable object.
        """
        if self.__end_value < (self.__start_value - 1):
            raise ValueError("end_value must be bigger than start_value")
        elif self.__end_value > (len(self.__iter_object) - 1):
            raise ValueError('end_value must be less than length of iterable object')
        elif self.__end_value >= self.__start_value:
            iteration = self.__iter_object[self.__start_value]
            self.__start_value += 1
            return iteration
        else:
            raise StopIteration


if __name__ == '__main__':
    list = [1, 2, 3, 4, 3, 5, 6]
    iterating = MyIterator(list, 0, 0)
    for i in iterating:
        print(i)
