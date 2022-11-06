import pytest
import random
import sys, os
from human import Human

sys.path.append(os.path.abspath('../HW20'))


@pytest.mark.xfail(reason='No age validation. Age cannot be less than zero. BUG')
@pytest.mark.negative
def test_create_human_with_negative_age(create_human_negative_age):
    with pytest.raises(Exception):
        human = create_human_negative_age


@pytest.mark.negative
def test_error_when_set_same_gender(create_valid_human):
    human, name = create_valid_human
    gender = human.gender
    with pytest.raises(Exception, match=f"{name} already has gender '{gender}'"):
        human.change_gender(gender)


@pytest.mark.negative
def test_change_gender_on_invalid(create_valid_human, faker):
    human, name = create_valid_human
    with pytest.raises(Exception, match='Not correct name of gender'):
        human.change_gender(name)


@pytest.mark.smoke
def test_human_death_after_100_year(human_have_100_years):
    human, name = human_have_100_years
    human.grow()
    with pytest.raises(Exception, match=f'{name} is already dead...'):
        human.grow()


@pytest.mark.xfail(reason='No name validation. Name cannot consist with number. BUG')
@pytest.mark.negative
def test_human_with_number_name(create_human_invalid_name):
    with pytest.raises(Exception):
        human = create_human_invalid_name


@pytest.mark.smoke
@pytest.mark.parametrize("gender", ['male', 'female'], ids=['from male to female', 'from female to male'])
def test_success_change_human_gender(access_to_genders, gender, faker):
    genders = access_to_genders
    human = Human(faker.name(), random.randint(0, 100), gender)
    gender_before_change = human.gender
    for element in genders:
        if element != human.gender:
            human.change_gender(element)
            break
    assert gender_before_change != human.gender


@pytest.mark.xfail(reason='No class initialization validation, BUG')
@pytest.mark.negative
def test_validation_during_initialization_instance(create_empty_human_instance):
    with pytest.raises(Exception):
        human = create_empty_human_instance


@pytest.mark.negative
def test_grow_human_with_string_age(create_human_with_string_age):
    human = create_human_with_string_age
    with pytest.raises(TypeError, match="'<' not supported between instances of 'str' and 'int'"):
        human.grow()


@pytest.mark.smoke
def test_check_grow_func(create_valid_human):
    human, name = create_valid_human
    age_before_func = human.age
    human.grow()
    assert human.age == age_before_func + 1, 'Function work wrong\n' \
                                             'Expected: after using grow() func, human instance ' \
                                             'will be older on 1 year'


@pytest.mark.smoke
def test_age(create_valid_human):
    human, name = create_valid_human
    assert 0 < human.age < 101, 'Human age are not valid!'
