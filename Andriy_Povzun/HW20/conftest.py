import random
from human import Human
import pytest

gender = ('male', 'famale')


@pytest.fixture
def create_valid_human(faker):
    return Human(faker.name(), random.randint(0, 100), random.choice(gender))


@pytest.fixture
def create_human_invalid_name():
    return Human(123, random.randint(0, 100), random.choice(gender))


@pytest.fixture
def create_human_negative_age(faker):
    return Human(faker.name(), -55, random.choice(gender))


@pytest.fixture
def human_grow_to_100_years(create_valid_human):
    human = create_valid_human
    while human.age != 100:
        human.grow()
    return human


@pytest.fixture
def create_empty_human_instance():
    return Human('', '', '')


@pytest.fixture
def create_human_with_string_age(faker):
    return Human(faker.name(), '22', random.choice(gender))
