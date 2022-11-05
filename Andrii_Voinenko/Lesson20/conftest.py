import pytest
from human import Human


@pytest.fixture()
def create_default_human():
    return Human('Jane', 55, 'female')


@pytest.fixture()
def create_custom_human_instance():
    def create_human(name: str, age: int, gender: str) -> Human:
        return Human(name, age, gender)

    return create_human


@pytest.fixture()
def human_dead_status(create_custom_human_instance):
    dead = create_custom_human_instance('Mitch', 100, 'male')
    dead.grow()
    return dead
