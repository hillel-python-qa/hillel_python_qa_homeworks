class Car:
    def __init__(self, brand: str, model: str, body_type: str, year: int, volume_of_engine: float, horse_power: int):
        self.__brand = brand
        self.__model = model
        self.__body_type = body_type
        self.__year = year
        self.__value_of_engine = volume_of_engine
        self.__horse_power = horse_power

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def body_type(self):
        return self.__body_type

    @property
    def year(self):
        return self.__year

    @property
    def volume_of_engine(self):
        return self.__value_of_engine

    @property
    def horse_power(self):
        return self.__horse_power

    def __str__(self):
        info = f"{self.__class__.__name__}:{{\n" \
               f"\tBrand: {self.__brand}\n" \
               f"\tModel: {self.__model}\n" \
               f"\tBody type: {self.__body_type}\n" \
               f"\tYear: {self.__year}\n" \
               f"\tVolume of engine: {self.__value_of_engine}\n" \
               f"\tNumber of horse pover: {self.__horse_power}\n}}"
        return info


if __name__ == '__main__':
    firstCar = Car("VW", "Golf 5", "Hatchback", 2007, 1.6, 102)
    print(firstCar)
