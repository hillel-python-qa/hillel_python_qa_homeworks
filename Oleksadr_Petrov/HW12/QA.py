from Oleksadr_Petrov.HW12.Employee import Employee


# inheritance
class QA(Employee):

    def __init__(self, grade: str, full_name: str, salary: float, position: str, assigned_testruns: list):
        # inheritance
        super(QA, self).__init__(grade, full_name, salary, position)
        # hiding
        self.__assigned_testruns = assigned_testruns

    # encapsulation
    @property
    def assigned_testruns(self):
        return self.__assigned_testruns

    # encapsulation
    @assigned_testruns.setter
    def assigned_testruns(self, assigned_testruns):
        if len(assigned_testruns) >= 5:
            raise Exception('QA cannot have more than 5 testruns')
        self.__assigned_testruns = assigned_testruns

    # polymorphism
    def work(self):
        print('Im work as QA')

    def test_execution(self, test_case_id: str):
        print('Im execute tc with id', test_case_id)






