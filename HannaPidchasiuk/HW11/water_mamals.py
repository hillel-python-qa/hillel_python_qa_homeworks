from HannaPidchasiuk.HW11.mamals import Mammals


class WaterMammal(Mammals):

    def __init__(self, species, number_of_subspecies, area_of_living, number_of_paws,
                 name_of_water_place: str):
        super().__init__(species, number_of_subspecies, area_of_living, number_of_paws)
        self.__name_of_water_place = name_of_water_place


