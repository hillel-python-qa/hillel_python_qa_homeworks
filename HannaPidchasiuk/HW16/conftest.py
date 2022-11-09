import pytest

from HannaPidchasiuk.HW16.human import Human


@pytest.fixture()
def create_human_custom():
    def create_human(name: str, age: int, gender: str):
        return Human(name, age, gender)
    return create_human

