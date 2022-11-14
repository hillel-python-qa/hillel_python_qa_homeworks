import pytest

from hillel_python_qa_homeworks.Olha_Lesiuk.HW_16.human import Human


@pytest.fixture()
def default_human():
    def create_default_human(name: str, age: int, gender: str):
        return Human(name, age, gender)
    return create_default_human
