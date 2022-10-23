class Train:
    def __init__(self):
        self.__head_of_train = "<=[HEAD]-"
        self.__wagons = self

    def head_of_train(self):
        return self.__head_of_train

    def wagons(self):
        value_of_wagons = []
        self.__wagons = value_of_wagons
        for value in range(1, 7):
            self.__wagons.append(f"[{value}]-")
        self.__wagons.insert(0, self.__head_of_train)
        return str(self.__wagons).replace("'", "").replace(",", "").replace(" ", "")

    def train_info(self):
        return self.__head_of_train, self.__wagons


if __name__ == '__main__':
    Train1 = Train()
    print(Train1.wagons())
