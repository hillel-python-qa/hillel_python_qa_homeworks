import random
import pytest


@pytest.mark.parametrize("gender, change_to", [("female", "male"), ("male", "female")],
                         ids=["female to male", "male to female"])
def test_change_gender_valid(create_human_custom, faker, gender, change_to):
    human = create_human_custom(faker.name(), random.randint(1, 99), gender)
    human.change_gender(change_to)

    assert human.gender == change_to, (f'Gender is not changed'
                                       f'\nActual: {human.gender}'
                                       f'\nExpected: {change_to}')


def test_change_gender_invalid(create_human_custom, faker):
    human = create_human_custom(faker.name(), random.randint(1, 99), "male")
    with pytest.raises(Exception, match="Not correct name of gender"):
        human.change_gender("snjf")


def test_change_gender_to_same(create_human_custom, faker):
    human = create_human_custom(faker.name(), 55, "male")
    with pytest.raises(Exception, match=f"{human._Human__name} already has gender '{human.gender}"):
        human.change_gender("male")


def test_human_grow_alive(create_human_custom, faker):
    age = random.randint(1, 99)
    human = create_human_custom(faker.name(), age, "male")
    human.grow()

    assert human.age == age + 1, (f'Age is not changed'
                                  f'\nActual: {human.age}'
                                  f'\nExpected: {age + 1}')
    assert human._Human__is_alive, (f'Human status is not alive'
                                    f'\nActual: {human._Human__status}'
                                    f'\nExpected: alive')


@pytest.mark.parametrize("age", [100, 101], ids=["start age 100", "start age 101"])
def test_human_status_dead(create_human_custom, faker, age):
    human = create_human_custom(faker.name(), age, "male")
    human.grow()

    assert human._Human__status == "dead", (f'Human status not changed to dead'
                                            f'\nActual: {human._Human__status}'
                                            f'\nExpected: dead')
    assert human.age == age, (f'Human age is changed, but should not'
                              f'\nActual: {human.age}'
                              f'\nExpected: {age}')
    with pytest.raises(Exception, match=f"{human._Human__name} is already dead..."):
        human._Human__is_alive()


@pytest.mark.skip(reason="No validation for age setter in Human")
def test_human_age_negative(create_human_custom, faker):
    with pytest.raises(ValueError):
        create_human_custom(faker.name(), -23, "male")


@pytest.mark.skip(reason="No validation for name setter in Human")
def test_human_name_empty(create_human_custom):
    with pytest.raises(ValueError):
        create_human_custom("", random.randint(1, 99), "female")


@pytest.mark.parametrize("age, gender", [
    (random.randint(1, 99), "male"),
    (random.randint(1, 99), "female")
], ids=["create valid male", "create valid female"])
def test_create_valid_human(create_human_custom, faker, age, gender):
    name = faker.name()
    human = create_human_custom(name, age, gender)

    assert human._Human__name == name, (f'Human name set incorrect'
                                        f'\nActual: {human._Human__name}'
                                        f'\nExpected: {name}')
    assert human.age == age, (f'Human age set incorrect'
                              f'\nActual: {human.age}'
                              f'\nExpected: {age}')
    assert human.gender == gender, (f'Human gender set incorrect'
                                    f'\nActual: {human.gender}'
                                    f'\nExpected: {gender}')


@pytest.mark.skip(reason="No validation for data types")
@pytest.mark.parametrize("name, age, gender", [
    (128937, 12, "male"),
    ("Name", "12", "female"),
    ("Name", 23, 3746)
], ids=["invalid name type", "invalid age type", "invalid gender type"])
def test_create_inavlid_human_data_types(create_human_custom, name, age, gender):
    with pytest.raises(Exception):
        create_human_custom(name, age, gender)
