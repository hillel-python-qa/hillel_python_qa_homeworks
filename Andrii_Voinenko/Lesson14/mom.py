from parent import Parent


# Inheritance
class Mom(Parent):
    def __init__(self, name: str, gender: str, age: int, health: str):
        super().__init__(name, gender, age)
        self.__health = health
        self.__child = False
        self.__child_age = 0
        self.__stamina = 100

    # Encapsulation
    def feeding(self):
        if self.__check_stamina():
            if self.__child:
                if 0 <= self.__child_age <= 1:
                    print(f'{self._name} feeding child with breasts')
                    self.__stamina -= 10
                    self.__child_age += 1
                else:
                    print(f'{self._name} can prepare a meal for her child')
                    self.__child_age += 1
                    self.__stamina -= 5
            else:
                print('Enjoy your life without child LOL')

    def __check_stamina(self):
        if self.__stamina < 30:
            print(f'{self._name} you need take a rest')
            return False
        return True

    def make_baby(self):
        if self.__health == ('good' or 'normal'):
            print(f'{self._name} can make a baby with a man')
            self.__child = True
        else:
            print(f'{self._name} for you are not recommended to make a baby')


if __name__ == '__main__':
    jane = Mom('Jane', 'Female', 18, 'good')

    jane.growing_up()
    jane.make_baby()
    jane.feeding()
    jane.feeding()
    jane.feeding()
    jane.feeding()
    jane.feeding()
    jane.feeding()