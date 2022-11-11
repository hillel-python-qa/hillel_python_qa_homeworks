import pytest
from human import Human


@pytest.fixture()
def create_human_instance():
    def create_human(name: str, age: int, gender: str):
        return Human
    return create_human


# @pytest.fixture()
# def create_dead_human_instance():

