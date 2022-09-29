from HannaPidchasiuk.HW11.area_of_living_enum import AreaOfLiving
from HannaPidchasiuk.HW11.mamals import Mammals


class FlyingMammals(Mammals):
    def __init__(self, species, number_of_subspecies, area_of_living, number_of_paws,
                 colour_of_feathers: str, ):
        super().__init__(species, number_of_subspecies, area_of_living, number_of_paws)
        self.__colour_of_feathers = colour_of_feathers

    @property
    def colour_of_feathers(self):
        """
            Returns colour of feathers of the flying mammal.
        """
        return self.__colour_of_feathers

    @colour_of_feathers.setter
    def colour_of_feathers(self, new_value):
        """
            Set new colour of feather of the flying mammal.
            Takes only 1 argument: new_value.
        """
        if new_value:
            self.__colour_of_feathers = new_value
        else:
            raise ValueError("colour_of_feathers can't be empty!")

    def go_to_warm_places(self, new_place: AreaOfLiving):
        """
            Move flying mammal to the new place.
        """
        warm_places = [AreaOfLiving.SAVANNA, AreaOfLiving.JUNGLE, AreaOfLiving.FOREST]
        water_places = [AreaOfLiving.RIVER, AreaOfLiving.SEA, AreaOfLiving.OCEAN]
        if new_place in water_places:
            print("Can't live in water!")
        elif self.area_of_living in warm_places:
            print("Already in warm place.")
        else:
            print(f"Move to {new_place.value}")


if __name__ == '__main__':
    owl = FlyingMammals("Owl", 10, AreaOfLiving.UNDERGROUND, 2, "grey")
    owl.subspecies_die()
    owl.found_new_subspecies()
    owl.go_to_warm_places(AreaOfLiving.FOREST)
