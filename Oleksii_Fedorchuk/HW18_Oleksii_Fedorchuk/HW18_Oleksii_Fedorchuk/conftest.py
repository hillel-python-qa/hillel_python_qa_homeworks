import pytest
from Project_Git.hillel_python_qa_homeworks.Oleksii_Fedorchuk.HW18_Oleksii_Fedorchuk.human import Human


@pytest.fixture()
def human_template():
    def create_human(name: str, age: int, gender: str):
        return Human(name, age, gender)

    yield create_human
