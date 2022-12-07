from random import randint

import pytest

from Mariia_Andanchenko.Homework20.human import Human


@pytest.fixture()
def create_custom_human_instance(faker) -> Human:
    def create_human(age, gender):
        return Human(faker.name(), age, gender)

    return create_human


@pytest.fixture()
def create_custom_human_gender_instance(faker) -> Human:
    def create_human(gender):
        return Human(faker.name(), randint(1, 99), gender)

    return create_human
