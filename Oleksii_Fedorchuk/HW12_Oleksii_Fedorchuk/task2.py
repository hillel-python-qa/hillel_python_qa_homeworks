class DescriptionOfPersons:
    """Description of worker/employees"""

    def __init__(self, name: str, age: int, position: str, salary: int, status: str, bio=None):
        self.__name = name
        self.__age = age
        self.__position = position
        self.__salary = salary
        self.__status = status
        self.__bio = bio

    def name_of_person(self):
        """Name of worker/employees"""

        name_of_person = self.__name
        print(name_of_person)

    def age_of_person(self):
        """Name of worker/employees"""

        age_of_person = self.__age
        print(age_of_person)

    def position_of_person(self):
        """Name of worker/employees"""

        position_of_person = self.__position
        print(position_of_person)

    def salary_of_person(self):
        """Name of worker/employees"""

        salary_of_person = self.__salary
        print(salary_of_person)

    def status_of_person(self):
        """Name of worker/employees"""

        status_of_person = self.__status
        print(status_of_person)

    def bio_of_person(self):
        """Full information of worker/employees"""

        bio_of_person = (f"Name of person: {self.__name}\n"
                         f"Age of person: {self.__age}\n"
                         f"Position of person: {self.__position}\n"
                         f"Salary of person: {self.__salary}\n"
                         f"Status of person: {self.__status}\n"
                         )
        print(bio_of_person)


if __name__ == "__main__":
    James = DescriptionOfPersons("James", 21, "QA", 1000, "Worker")
    # James.name_of_person()
    # James.age_of_person()
    # James.position_of_person()
    # James.salary_of_person()
    # James.status_of_person()
    James.bio_of_person()
    Jane = DescriptionOfPersons("Jane", 32, "TeamLead", 3000, "Employee")
    # Jane.name_of_person()
    # Jane.age_of_person()
    # Jane.position_of_person()
    # Jane.salary_of_person()
    # Jane.status_of_person()
    Jane.bio_of_person()
