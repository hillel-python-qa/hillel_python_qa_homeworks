import pytest


@pytest.mark.xfail(reason='No age validation. Age cannot be less than zero. BUG')
@pytest.mark.negative
def test_create_human_with_negative_age(create_human_negative_age):
    with pytest.raises(Exception):
        human = create_human_negative_age


@pytest.mark.negative
def test_error_when_set_same_gender(create_valid_human):
    human = create_valid_human
    gender = human.gender
    with pytest.raises(Exception):
        human.change_gender(gender)


@pytest.mark.negative
def test_change_gender_on_invalid(create_valid_human):
    human = create_valid_human
    with pytest.raises(Exception):
        human.change_gender('bla')


@pytest.mark.negative
def test_human_grow_after_100_year(human_grow_to_100_years):
    human = human_grow_to_100_years
    human.grow()
    assert human.age == 100
    with pytest.raises(Exception):
        human.grow()


@pytest.mark.xfail(reason='No name validation. Name cannot consist with number. BUG')
@pytest.mark.negative
def test_human_with_number_name(create_human_invalid_name):
    with pytest.raises(Exception):
        human = create_human_invalid_name


@pytest.mark.smoke
def test_success_change_human_gender(create_valid_human):
    male = 'male'
    female = 'female'
    human = create_valid_human
    if human.gender == male:
        human.change_gender(female)
        assert human.gender == female
    else:
        human.change_gender(male)
        assert human.gender == male


@pytest.mark.xfail(reason='No class initialization validation, BUG')
@pytest.mark.negative
def test_validation_during_initialization_instance(create_empty_human_instance):
    with pytest.raises(Exception):
        human = create_empty_human_instance


@pytest.mark.negative
def test_grow_human_with_string_age(create_human_with_string_age):
    human = create_human_with_string_age
    with pytest.raises(Exception):
        human.grow()


@pytest.mark.smoke
def test_check_grow_func(create_valid_human):
    human = create_valid_human
    age_before_func = human.age
    human.grow()
    assert human.age == age_before_func + 1
