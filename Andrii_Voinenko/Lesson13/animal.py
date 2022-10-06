class Animals:
    def __init__(self, name: str, gender: str, health: str):
        self._name = name
        self._gender = gender
        self._health = health
        self._feeding = None

        if self._health not in ['bad', 'normal', 'good']:
            raise TypeError('Set correct value for health: bad, normal or good')

    def creature_death(self):
        if self._health == 'bad':
            return False
        else:
            return True

    def creature_mating(self):
        if self._health == 'bad':
            print('Health of the creature is too bad for mating')
            self._feeding = True
            return self._feeding
