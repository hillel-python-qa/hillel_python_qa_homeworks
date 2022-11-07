import random
from human import Human
import pytest

genders = ('male', 'female')


@pytest.fixture
def create_valid_human(faker):
    name = faker.name()
    return Human(name, random.randint(0, 100), random.choice(genders)), name


@pytest.fixture
def create_human_invalid_name():
    return Human(123, random.randint(0, 100), random.choice(genders))


@pytest.fixture
def create_human_negative_age(faker):
    return Human(faker.name(), -55, random.choice(genders))


@pytest.fixture
def human_have_100_years(faker):
    name = faker.name()
    return Human(name, 100, random.choice(genders)), name


@pytest.fixture
def create_empty_human_instance():
    return Human('', '', '')


@pytest.fixture
def create_human_with_string_age(faker):
    return Human(faker.name(), '22', random.choice(genders))


@pytest.fixture
def access_to_genders():
    return genders
