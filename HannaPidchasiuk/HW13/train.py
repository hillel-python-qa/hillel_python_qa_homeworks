class Train:

    def __init__(self, wagons: list[int]):
        self.__wagons = wagons

    def __len__(self):
        return len(self.__wagons)

    def __str__(self):
        train_to_print = '<=[HEAD]'
        for wagon in sorted(self.__wagons):
            train_to_print += f"-[{wagon}]"
        return train_to_print

    @property
    def wagons(self):
        return self.__wagons

    @wagons.setter
    def wagons(self, value: int):
        if value in self.__wagons:
            raise ValueError("Such wagon already exists!")
        elif value < 1:
            raise ValueError("Wagon number can't be less than 1!")
        else:
            self.__wagons.append(value)


if __name__ == '__main__':
    wagons_list = [1, 3, 4, 5, 6, 2, 9, 7, 8]

    train = Train(wagons_list)
    print(train)
    print(len(train))

