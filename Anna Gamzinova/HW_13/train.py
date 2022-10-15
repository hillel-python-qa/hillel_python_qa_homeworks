from wagons import Wagon


class Train(Wagon):
    def __init__(self, wagons: int, passengers: int):
        super().__init__(wagons, passengers)

    def __len__(self):
        return self.wagons

    def add_wagon(self, new_wagon_number: int = 1):
        """
        A method to add the number of passengers
        """
        if type(new_wagon_number) == int and new_wagon_number > 0:
            self.__wagons += new_wagon_number
        else:
            print("The new new wagon's number should be numeric  ")


if __name__ == '__main__':
    my_train = Train(10, 5)
    print(len(my_train))
