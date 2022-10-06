class TrainWagon:
    def __init__(self, wagon_number: int):
        self._wagon_number = wagon_number
        self._passengers = []

    @property
    def wagon_number(self):
        return self._wagon_number

    @property
    def passengers(self):
        if not self._passengers:
            raise Exception('Wagon is empty.')
        else:
            return self._passengers

    def add_passenger(self, passenger_name: str, passenger_surname: str):
        if len(self._passengers) == 10:
            raise Exception('In wagon not have free places ')
        elif (passenger_name, passenger_surname) in self._passengers:
            raise Exception('This human already located in wagon')
        self._passengers.append((passenger_name, passenger_surname))

    def __len__(self):
        return len(self._passengers)

    def __str__(self):
        return f'{[self._wagon_number]}'
