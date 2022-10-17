class Employee:
    def __init__(self, name, age, gender, position):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__position = position

    def __str__(self):
        return f'{Employee.__name__}: {{\n\t\t\tname: {self.__name},' \
               f'\n\t\t\tage: {self.__age},' \
               f'\n\t\t\tgender: {self.__gender},' \
               f'\n\t\t\tposition: {self.__position}\n}}'


if __name__ == '__main__':
    sarah = Employee('Sarah', 25, 'f', 'middle')
    print(sarah)
