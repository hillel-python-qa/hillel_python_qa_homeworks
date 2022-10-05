# import
from hillel_python_qa_homeworks.Olha_Lesiuk.HW_11.Predatory import Predatory


# class inheritance

home = "Jungle"


class Lion(Predatory):
    # instance attribute

    # encapsulation
    # hiding
    def __init__(self, kingdom: str, specie_type: str, mammals_types: str,
                 predatory_types: str, wool_is_present: bool, name: str):
        super().__init__(kingdom, specie_type, mammals_types, predatory_types, wool_is_present, name)
        self.__kingdom = kingdom
        self.__specie_type = specie_type
        self.__mammals_types = mammals_types
        self.__predatory_types = predatory_types
        self.__wool_is_present = wool_is_present
        self.__name = name

# polymorphism
    @staticmethod
    def moving():
        print("Lions can run")


class Snake(Predatory):
    # instance attribute

    # encapsulation
    # hiding
    def __init__(self, kingdom: str, specie_type: str, mammals_types: str,
                 predatory_types: str, wool_is_present: bool, name: str):
        super().__init__(kingdom, specie_type, mammals_types, predatory_types, wool_is_present, name)
        self.__kingdom = kingdom
        self.__specie_type = specie_type
        self.__mammals_types = mammals_types
        self.__predatory_types = predatory_types
        self.__wool_is_present = wool_is_present
        self.__name = name

# polymorphism
    @staticmethod
    def moving():
        print("Snakes can crowl")
# instantiate objects


if __name__ == '__main__':
    lion = Lion(kingdom="Animals", specie_type="Mammals", mammals_types="Predatory",
                predatory_types="Carnivore", wool_is_present=True, name="Lion")
    snake = Snake(kingdom="Animals", specie_type="Mammals", mammals_types="Predatory",
                  predatory_types="Carnivore", wool_is_present=False, name="Snake")

# passing the object
    print(lion.name)
    print(snake.name)
    lion.moving()
    snake.moving()
    print(f'They live in {home}')
