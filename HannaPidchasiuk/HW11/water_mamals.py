import certifi
import geopy
import re
import ssl

from geopy.geocoders import Nominatim

from HannaPidchasiuk.HW11.area_of_living_enum import AreaOfLiving
from HannaPidchasiuk.HW11.mamals import Mammals


class WaterMammal(Mammals):

    def __init__(self, species, number_of_subspecies, area_of_living, number_of_paws,
                 name_of_water_place: str):
        super().__init__(species, number_of_subspecies, area_of_living, number_of_paws)
        self.__name_of_water_place = name_of_water_place

    @property
    def name_of_water_place(self):
        """
            Returns name of water place of the water mammal.
        """
        return self.__name_of_water_place

    @name_of_water_place.setter
    def name_of_water_place(self, new_value: str):
        """
            Set name of water place of the water mammal.
            Takes only 1 argument: new_value.
        """
        if new_value:
            self.__name_of_water_place = new_value
        else:
            raise ValueError("name_of_water_place can't be empty!")

    @staticmethod
    def __extract_coordinates(coord: str):
        """
            Check if coordinates are correct and if there are extra symbols - removes it.
        """
        pattern = re.compile(r"([0-9]+\.[0-9]+)|(-[0-9]+\.[0-9]+)")
        find_all = re.findall(pattern, coord)
        if not find_all:
            print(f"{coord} not  coordinate!")
        else:
            temp_coord = 0
            for item in find_all[0]:
                if item:
                    temp_coord = item
            return temp_coord

    def get_coordinates(self):
        """
            Getting of coordinates of water place location.
        """
        geopy.geocoders.options.default_ssl_context = ssl.create_default_context(cafile=certifi.where())
        loc = Nominatim(user_agent="GetLoc")
        get_loc = loc.geocode(self.__name_of_water_place)
        return get_loc.latitude, get_loc.longitude

    def set_water_place_by_coord(self, latitude: str, longitude: str):
        """
            Set water place by provided coordinates.
            Name of tha water place will be set in local language of this water place.
        """
        geopy.geocoders.options.default_ssl_context = ssl.create_default_context(cafile=certifi.where())
        get_loc = Nominatim(user_agent="GetLoc")
        latitude_checked = self.__extract_coordinates(latitude)
        longitude_checked = self.__extract_coordinates(longitude)
        if latitude_checked and longitude_checked:
            self.__name_of_water_place = get_loc.reverse(
                f"{longitude_checked}, {longitude_checked}")
        else:
            print("Incorrect data provided!")


if __name__ == "__main__":
    whale = WaterMammal("Whale", 10, AreaOfLiving.OCEAN, 0, "Atlantic ocean")
    print(whale.get_coordinates())
    whale.set_water_place_by_coord("27.378443", "12.993815")
    print(whale.name_of_water_place)
