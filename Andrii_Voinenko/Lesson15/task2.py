class Train:
    def __init__(self, wagons: list[int]):
        self.__wagons = wagons

    @property
    def wagon(self):
        return self.__wagons

    @wagon.setter
    def wagon(self, wagon: int):
        if wagon in self.__wagons:
            raise ValueError(f'Entered wagon number: {wagon} is present in sequence')
        elif wagon < 1:
            raise ValueError('Wagon number cannot be less then 1')
        else:
            self.__wagons.append(wagon)

    def __str__(self):
        head_of_train = '<=[HEAD]'
        for wagon in sorted(self.__wagons):
            head_of_train += f"-[{wagon}]"
        return head_of_train

    def __len__(self):
        return self.__wagons


class TrainCar:
    def __init__(self, passengers: list[str]):
        self.__passengers = passengers

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, new_passenger: str):
        if new_passenger in self.__passengers:
            raise Exception('One ticket for one passenger')
        elif type(new_passenger) != str:
            raise TypeError('Only string in format: Name')
        else:
            self.__passengers.append(new_passenger)

    def __len__(self):
        return f'Current in wagon {len(self.__passengers)}'


if __name__ == '__main__':
    hogwarts_express = Train([1, 2, 3, 4, 5, 6])
    hogwarts_express_passengers = TrainCar(['Harry', 'Ron', 'Hermiona'])

    hogwarts_express_passengers.passengers = 'Drako'
    print(hogwarts_express_passengers.passengers)
    print(hogwarts_express)
    print(hogwarts_express.__len__())
