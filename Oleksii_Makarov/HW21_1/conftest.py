import pytest
from human import Human



@pytest.fixture()
def create_custom_human():
    def create_human_instance_insert(name: str, age: int, gender: str):
        return Human(name, age, gender)

    return create_human_instance_insert
