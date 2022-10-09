class Wagon:

    def __init__(self, wagon_number: int, passengers: list[str]):
        self.__wagon_number = wagon_number
        self.__passengers = passengers

    def __len__(self):
        return len(self.__passengers)

    def __str__(self):
        return f"[{self.__wagon_number}]"

    @property
    def wagon_number(self):
        return self.__wagon_number

    @wagon_number.setter
    def wagon_number(self, value: int):
        if value < 1:
            raise ValueError("Wagon number can't be less than 1!")
        else:
            self.__wagon_number = value

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, value: str):
        if value:
            self.__passengers.append(value)
        else:
            raise ValueError("Value can't be empty!")


if __name__ == '__main__':
    passengers_list = [
        "Name0 Surname",
        "Name1 Surname",
        "Name2 Surname",
        "Name3 Surname",
        "Name4 Surname",
        "Name5 Surname",
        "Name6 Surname",
        "Name7 Surname",
        "Name8 Surname",
        "Name9 Surname",
    ]
    wagon = Wagon(2, passengers_list)

    print(len(wagon))
    print(wagon)
