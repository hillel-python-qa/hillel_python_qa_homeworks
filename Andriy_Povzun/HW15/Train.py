from TrainWagon import TrainWagon

number_wagon_generator = (number for number in range(1, 1000))


class Train:
    def __init__(self):
        self._wagons = []

    def __str__(self):
        i = 0
        head = '<=[HEAD]-'
        while i < len(self._wagons):
            if self._wagons[i].wagon_number == len(self._wagons):
                head += f'{self._wagons[i]}'
                i += 1
            else:
                head += f'{self._wagons[i]}-'
                i += 1
        return head

    def __len__(self):
        if not self._wagons:
            raise Exception('Now train without wagon')
        return len(self._wagons)

    def add_wagon(self):
        new_wagon = TrainWagon(next(number_wagon_generator))
        self._wagons.append(new_wagon)

    @property
    def wagons(self):
        return self._wagons


if __name__ == '__main__':
    train = Train()
    train.add_wagon()
    train.add_wagon()
    train.wagons[0].add_passenger('Andriy', 'Povzun')
    train.wagons[1].add_passenger('Lina', 'Povzun')
    print(train.wagons[0].passengers)
    print(train)
    print(len(train))
