# import
from hillel_python_qa_homeworks.Olha_Lesiuk.HW_11.Predatory import Predatory
# class inheritance


class Lion(Predatory):
    def __init__(self, kingdom: str, specie_type: str, mammals_types: str,
                 predatory_types: str, wool_is_present: bool, name: str):
        super().__init__(kingdom, specie_type, mammals_types, predatory_types, wool_is_present, name)
        self.__kingdom = kingdom
        self.__specie_type = specie_type
        self.__mammals_types = mammals_types
        self.__predatory_types = predatory_types
        self.__wool_is_present = wool_is_present
        self.__name = name
