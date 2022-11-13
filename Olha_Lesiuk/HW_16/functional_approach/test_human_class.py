import random

import pytest


# test if the app accepts valid Human data in general
def test_valid_human_data(default_human, faker, gender):
    age = random.randint(0, 99)
    name = faker.name()
    human = default_human(name, age, 'male')
    assert human._Human__name == name, (f'The name is invalid'
                                        f'\nActual: {human._Human.__name}'
                                        f'\nExpected: {name}')
    assert human.age == age, (f'The age is invalid'
                              f'\nActual: {human.age}'
                              f'\nExpected: {age}')
    assert human.gender == gender, (f'The gender is invalid'
                                    f'\nActual: {human.gender}'
                                    f'\nExpected: {gender}')


def test_age_below_the_limit(default_human, faker):
    age = random.randint(0, 99)
    human = default_human(faker.name(), age, 'male')
    human.grow()
    assert human.age == age + 1, (f'Age is below the limit'
                                  f'\nActual: {human.age}'
                                  f'\nExpected: {age + 1}')

# test if the man is not marked alive if he is above the limit age: more than 100


def test_age_above_the_limit(default_human, faker):
    age = random.randint(100, 110)
    human = default_human(faker.name(), age, 'male')
    human.grow()
    assert human.age == age, (f'Age is above the limit age'
                              f'\nActual: {human.age}'
                              f'\nExpected: {age}')
    with pytest.raises(Exception, match=f"{human._Human__name} is already dead..."):
        human._Human__is_alive()

# test the man is not marked alive if he enters invalid value: with minus


@pytest.mark.xfail(reason='The age is not acceptable, the value is invalid')
@pytest.mark.negative
def test_invalid_age_value(default_human, faker):
    with pytest.raises(ValueError):
        default_human(faker.name(), -5, 'male')

# test if the user enter letters in the age field


@pytest.mark.xfail(reason='The age is invalid and field accepts only digits')
@pytest.mark.negative
def test_if_enter_letters_in_age(default_human, faker):
    with pytest.raises(ValueError):
        default_human(faker.name(), 'sadsd', 'male')

# test if the app accepts valid values: male or female


@pytest.mark.parametrize('gender, switch_gender', [('male', 'female'), ('female', 'male')],
                         ids=['male to female', 'female to male'])
def test_valid_gender(default_human, faker, gender, switch_gender):
    age = random.randint(1, 99)
    human = default_human(faker.name(), age, gender)
    human.change_gender(switch_gender)
    assert human.gender == switch_gender, (f'The gender is the same'
                                           f'\nActual: {human.gender}'
                                           f'\nExpected: {switch_gender}')

# test if the user try to enter the same gender


def test_if_the_name_gender_is_correct(default_human, faker):
    age = random.randint(1, 99)
    human = default_human(faker.name(), age, 'female')
    with pytest.raises(Exception, match="Not correct name of gender"):
        human.change_gender('It')

# test if the user doesn't feel in the gender field


@pytest.mark.xfail(reason='The age is should not be empty')
@pytest.mark.negative
def test_if_dont_feel_gender(default_human, faker):
    with pytest.raises(ValueError):
        default_human(faker.name(), 50, '')

# test if the user enter digits in the gender field


@pytest.mark.negative
def test_if_enter_digits_in_gender(default_human, faker):
    with pytest.raises(ValueError):
        default_human(faker.name(), 50, '2193')
