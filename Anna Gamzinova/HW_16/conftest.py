import pytest
from human import Human


@pytest.fixture()
def create_human_instance():
    def create_human(name: str, age: int, gender: str):
        return Human(name, age, gender)

    return create_human

