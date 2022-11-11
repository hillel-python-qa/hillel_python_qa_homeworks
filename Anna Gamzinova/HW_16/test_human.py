import random
import faker
import pytest
from faker import Faker



@pytest.mark.parametrize("age", "gender", [(random.randint(1, 99), "male"), (random.randint(1, 99), "female")],
                         ids=["create male human", "create female human"])
def test_create_human(create_human_instance, faker, age, gender):
    fake = Faker()
    name = fake.name
    human = create_human_instance(name, age, gender)

    assert human._Human_name == name

    assert human.age == age

    assert human.gender == gender


