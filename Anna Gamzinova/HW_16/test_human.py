import random
import pytest
import string


@pytest.mark.create_human
@pytest.mark.parametrize("age, gender", [(random.randint(1, 99), "male"), (random.randint(1, 99), "female")],
                         ids=["create male human", "create female human"])
def test_create_human(create_human_instance, faker, age, gender):
    name = faker.name()
    human = create_human_instance(name, age, gender)
    assert human._Human__name == name, (f'Wrong name'
                                        f'\nActual result: {human._Human.__name}'
                                        f'\nExpected result: {name}')

    assert human.age == age, (f"Wrong age"
                              f'\nActual result: {human.age}'
                              f'\nExpected result: {age}')

    assert human.gender == gender, (f"Wrong gender"
                                    f'\nActual result: {human.gender}'
                                    f'\nExpected result: {gender}')


@pytest.mark.invalid_human
@pytest.mark.skip(reason="Incorrect validation")
@pytest.mark.parametrize("name, age, gender", [(random.randint(1, 100), random.randint(1, 99), "female"),
                                               ("Anna", string.ascii_letters, "female"),
                                               ("Anna", random.randint(1, 99), string.ascii_letters)],
                         ids=["invalid name", "invalid age", "invalid gender"])
def test_create_invalid_human(create_human_instance, name, age, gender):
    with pytest.raises(Exception):
        create_human_instance(name, age, gender)


@pytest.mark.grow
def test_human_grow(create_human_instance, faker):
    name = faker.name()
    age = random.randint(1, 99)
    my_human = create_human_instance(name, age, "female")
    my_human.grow()

    assert my_human.age == age + 1, (f'Age has not been changed'
                                     f'\nExpected result: {age + 1}'
                                     f'\nActual result: {my_human.age} ')

    assert my_human._Human__is_alive, (f'Wrong human status'
                                       f'\nExpected result : alive '
                                       f'\nActual result: {my_human._Human__status}')


@pytest.mark.dead
def test_human_dead(create_human_instance, faker):
    name = faker.name()
    age = random.randint(100, 1000)
    dead_human = create_human_instance(name, age, "male")
    dead_human.grow()

    assert dead_human._Human__status == "dead", (f'The human status has not been changed'
                                                 f"\nExpected result:dead"
                                                 f'\nActual result: {dead_human._Human__status}')

    assert dead_human.age == age, f'Not supported age value'

    with pytest.raises(Exception, match=f'{dead_human._Human__name} is already dead...'):
        dead_human._Human__is_alive()


@pytest.mark.change_gender
@pytest.mark.parametrize("gender,new_gender", [("male", "female"), ("female", "male")],
                         ids=["male to female", "female to male"])
def test_change_gender(create_human_instance, faker, gender, new_gender):
    human = create_human_instance(faker.name(), random.randint(1, 99), gender)
    human.change_gender(new_gender)

    assert human.gender == new_gender, (f"Gender has not been changed"
                                        f"\nExpected result: {new_gender}"
                                        f"\nActual result: {human.gender}")


@pytest.mark.wrong_gender_change
def test_change_gender_to_wrong(create_human_instance, faker):
    human = create_human_instance(faker.name(), random.randint(1, 99), "female")
    with pytest.raises(Exception, match="Not correct name of gender"):
        human.change_gender("femal")


@pytest.mark.same_gender
def test_change_same_gender(create_human_instance, faker):
    human = create_human_instance(faker.name(), random.randint(1, 99), "female")
    with pytest.raises(Exception, match=f"{human._Human__name} already has gender '{human.gender}'"):
        human.change_gender("female")


@pytest.mark.negative_age
@pytest.mark.skip(reason="Incorrect validation")
def test_negative_age(create_human_instance, faker):
    with pytest.raises(ValueError):
        create_human_instance(faker.name(), -2, "male")
