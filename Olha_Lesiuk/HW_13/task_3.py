from hillel_python_qa_homeworks.Olha_Lesiuk.HW_13.task_2 import TrainStructure


class Train(TrainStructure):

    def __init__(self, wagons_list: list[int], wagon_number: int, amount_of_passengers: list[str]):
        super().__init__(wagon_number, amount_of_passengers)
        self.__wagons = wagons_list

    @property
    def wagon_number(self):
        return self.__wagons

    @wagon_number.setter
    def wagon_number(self, number: int):
        if number < 1:
            raise ValueError("Enter a valid wagon's number!")
        else:
            self.__wagons.append(number)

    def __len__(self):
        return len(self.__wagons)

    def __str__(self):
        test_print = "<+[HEAD]"
        for wagon in sorted(self.__wagons):
            test_print += f'-[{wagon}]'
        return test_print


if __name__ == '__main__':
    passengers = ["Unknown", "Unknown", "Unknown", "Unknown"]
    wagon_list = [1, 2, 3, 4, 5]
    train = TrainStructure(9, passengers)
    train_details = Train(wagon_list, 9, ["Unknown", "Unknown", "Unknown", "Unknown"])
    print(train_details)
