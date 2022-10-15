class Wagons:
    def __init__(self, wagons: int, passengers: int):
        if (type(wagons) == int) and wagons > 0:
            self.__wagons = wagons
        else:
            raise ValueError("The wagon's number should be numeric")
        if (type(passengers) == int) and passengers > 0:
            self.__passengers = passengers
        else:
            raise ValueError("The passengers number should be numeric")

    @property
    def wagons(self):
        return self.__wagons

    @wagons.setter
    def wagons(self, new_wagons_number):
        if (type(new_wagons_number) == int) and new_wagons_number > 0:
            self.__wagons = new_wagons_number
        else:
            print("The new wagon's number should be numeric and higher than 0")

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, new_passengers_number):
        if (type(new_passengers_number) == int) and new_passengers_number > 0:
            self.__passengers = new_passengers_number
        else:
            print("The new passenger's number should be numeric and higher than 0")

    def add_passenger(self, passenger_number: int = 1):
        """
        A method to add the number of passengers
        """
        if type(passenger_number) == int and passenger_number > 0 and (self.__passengers + passenger_number) < 11:
            self.__passengers += passenger_number
        else:
            print("The new passenger's number should be numeric.")

    def __len__(self):
        return self.__passengers


if __name__ == '__main__':
    wagon = Wagons(3, 5)
    print(len(wagon))
    wagon.add_passenger(2)
    print(wagon.passengers)

