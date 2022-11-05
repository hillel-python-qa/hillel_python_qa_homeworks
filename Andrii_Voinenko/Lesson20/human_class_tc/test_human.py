import pytest


def test_grow_up(create_custom_human_instance):
    human = create_custom_human_instance('Oleh', 19, 'male')
    human.grow()

    assert human.age == 20, (f'1 year was not added\n'
                             f'Actual result: {human.grow()}\n'
                             f'Expected result: 20')


@pytest.mark.skip(reason='No validation for negative number')
def test_negative_age(create_custom_human_instance):
    human = create_custom_human_instance('May', -2, 'female')
    with pytest.raises(Exception):
        human.grow()


def test_str_instead_int_for_age(create_custom_human_instance):
    human = create_custom_human_instance('Olaf', '19', 'male')
    with pytest.raises(TypeError):
        human.grow()


def test_grow_up_for_dead_human(human_dead_status):
    human = human_dead_status
    with pytest.raises(Exception):
        human.grow()


@pytest.mark.parametrize('wrong_gender', ['Male', 'Female', 1, '1'])
def test_gender_validation_with_alive_status(create_custom_human_instance, wrong_gender):
    human = create_custom_human_instance('Joan', 20, 'female')
    with pytest.raises(Exception):
        human.change_gender(wrong_gender)


def test_gender_validation_with_dead_status(human_dead_status):
    human = human_dead_status
    with pytest.raises(Exception):
        human.change_gender('female')


def test_gender_validation_for_same_gender(create_default_human):
    human = create_default_human
    with pytest.raises(Exception):
        human.change_gender('female')


def test_change_gender(create_default_human):
    human = create_default_human
    change_gender = human.change_gender('male')

    assert human.gender == 'male', (f'Gender was not changed\n'
                                    f'Actual result: {change_gender}\n'
                                    f'Expected result: male')
