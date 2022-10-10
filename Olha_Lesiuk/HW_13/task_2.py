class TrainStructure:

    def __init__(self, wagon_number: int, amount_of_passengers: list[str]):
        self.__wagon_number = wagon_number
        self.__amount_of_passengers = amount_of_passengers

    @property
    def wagon_number(self):
        return self.__wagon_number

    @wagon_number.setter
    def wagon_number(self, wagon_number):
        if wagon_number < 1:
            raise ValueError("Please, choose the valid wagon's number!")
        else:
            self.__wagon_number = wagon_number

    @property
    def amount_of_passengers(self):
        if self.__amount_of_passengers:
            return self.__amount_of_passengers
        else:
            raise ValueError("The wagon is not filled in with passengers")

    @amount_of_passengers.setter
    def amount_of_passengers(self, passenger_data: str):
        if passenger_data:
            self.__amount_of_passengers.append(passenger_data)
        else:
            raise ValueError("You should fill in valid passenger name and surname!")

    def __len__(self):
        return self.__amount_of_passengers

    def __str__(self):
        return f'[{self.__wagon_number}]'


if __name__ == '__main__':
    passengers = ["Unknown", "Unknown", "Unknown", "Unknown"]
    train = TrainStructure(9, passengers)
    print(len(passengers))
    print(train)
