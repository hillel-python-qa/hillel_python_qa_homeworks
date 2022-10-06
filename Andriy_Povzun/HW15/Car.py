class Car:
    def __init__(self, body_type: str, brand: str, model: str):
        self.__body_type = body_type
        self.__brand = brand
        self.__model = model

    @property
    def body_type(self):
        return self.__body_type

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    def __str__(self):
        result = f'{self.__class__.__name__}\n{{' \
                 f'\tBody type: {self.__body_type}\n' \
                 f'\tBrand: {self.__brand}\n' \
                 f'\tModel: {self.__model}\n}}'
        return result


if __name__ == '__main__':
    car = Car('Sedan', 'BMW', '535i')
    print(car)
