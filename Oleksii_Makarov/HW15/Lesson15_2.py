import re


class Train:
    def __init__(self, length: list):
        self.__length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length.append(value)

    def __len__(self):
        return len(self.__length)

    def __str__(self):
        train_head = f'<=[HEAD]'
        for i in self.__length:
            train_head += f'-{i}'
        return train_head

    def add_wagon(self, number, pass_list):
        pass


class TrainCar:
    def __init__(self, wagons: int, passengers: list):
        self.__wagons = wagons
        self.__passengers = passengers

    @property
    def wagons(self):
        return self.__wagons

    @wagons.setter
    def wagons(self, wagons_value):
        if type(wagons_value) == int and wagons_value > 0:
            self.__wagons = wagons_value
        else:
            raise ValueError('wagons_value must be a positive int')

    @property
    def passengers(self):
        return self.__passengers

    def passengers_adder(self, passengers_value: str):
        if re.search(r'\S', passengers_value):
            self.__passengers.append(passengers_value)
        else:
            raise ValueError("New passengers names must be a string")

    def __len__(self):
        return len(self.__passengers)

    def __str__(self):
        return f'[{self.__wagons}]'


if __name__ == '__main__':
    passeng = ['Name1', 'Name2', 'Name3', 'Name4', ]
    traincar = TrainCar(3, passeng)
    traincar2 = TrainCar(2, passeng)
    traincar3 = TrainCar(1, passeng)
    print(traincar)
    print(len(traincar))
    wagons = [traincar, traincar2, traincar3]
    train = Train(wagons)
    print(train)
    print(len(train))
