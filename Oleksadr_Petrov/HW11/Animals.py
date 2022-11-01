class Animals:

    def __init__(self, species: str, age: int, voice: str, food_preferences: str, fly_possibility: bool,
                 way_of_procreation: str):
        self.__species = species
        self.__age = age
        self.__voice = voice
        self.__food_preferences = food_preferences
        self.__fly_possibility = fly_possibility
        self.__way_of_procreation = way_of_procreation

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, species):
        self.__species = species

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def voice(self):
        return self.__species

    @voice.setter
    def voice(self, voice):
        self.__voice = voice

    @property
    def food_preferences(self):
        return self.__food_preferences

    @food_preferences.setter
    def food_preferences(self, food_preferences):
        self.__food_preferences = food_preferences

    @property
    def fly_possibility(self):
        return self.__fly_possibility

    @fly_possibility.setter
    def fly_possibility(self, fly_possibility):
        self.__fly_possibility = fly_possibility

    @property
    def way_of_procreation(self):
        return self.__way_of_procreation

    @way_of_procreation.setter
    def way_of_procreation(self, way_of_procreation):
        self.__way_of_procreation = way_of_procreation

    def make_a_sound(self):
        print(self.__voice)

    def move(self):
        print('I\'m move like Animal!')
