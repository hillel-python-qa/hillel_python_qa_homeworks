class Shoes:
    def __init__(self, brand: str, size: int, colour: str):
        self.__brand = brand
        self.__size = size
        self.__colour = colour

    def __str__(self):
        obj = f'{self.__class__.__name__}: {{\n' \
              f'\tbrand: {self.__brand}\n' \
              f'\tsize: {self.__size}\n' \
              f'\tcolour: {self.__colour}\n}}'
        return obj

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_value):
        if new_value:
            self.__brand = new_value
        else:
            raise ValueError("Brand can't be empty!")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_value):
        if new_value > 0:
            self.__size = new_value
        else:
            raise ValueError("Size can't be 0 or less than 0!")

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, new_value):
        if new_value:
            self.__colour = new_value
        else:
            raise ValueError("Colour can't be empty!")


if __name__ == '__main__':
    shoes = Shoes('Nike', 38, 'Black')
    print(shoes)
