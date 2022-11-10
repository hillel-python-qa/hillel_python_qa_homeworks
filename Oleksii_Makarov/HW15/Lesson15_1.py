import re


class Phone:
    def __init__(self, size: float, battery_mAh: int, color: str):
        self.__size = size
        self.__battery_mAh = battery_mAh
        self.__color = color

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size_value):
        if type(size_value) == float and size_value > 0:
            self.__size = size_value
        else:
            raise TypeError("size_value must be a positive float")

    @property
    def battery_mAh(self):
        return self.__battery_mAh

    @battery_mAh.setter
    def battery_mAh(self, battery_value):
        if type(battery_value) == int and battery_value > 0:
            self.__battery_mAh = battery_value
        else:
            raise TypeError("battery_value must be a positive int")

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color_value):
        if re.search(r'\S', color_value):
            self.__color = color_value
        else:
            raise ValueError("color value must be filled")

    def __str__(self):
        smartphone = f'{self.__class__.__name__}: {{\n'\
                     f'\tsize:{self.__size}\n' \
                     f'\tbattery in mAh: {self.__battery_mAh}\n' \
                     f'\tcolor: {self.__color}\n}}'
        return smartphone


if __name__ == '__main__':
    samsung = Phone(5.3, 6000, "black")
    print(samsung)
