from random import randint

import pytest


@pytest.mark.parametrize("current_gender, new_gender", [("female", "male"), ("male", "female")],
                         ids=['female_to_male', 'male_to_female'])
def test_change_new_gender(create_custom_human_gender_instance, current_gender, new_gender):
    human = create_custom_human_gender_instance(current_gender)
    human.change_gender(new_gender)
    assert human.gender == new_gender, (f'New video was not added'
                                        f'\nActual: {human.gender}'
                                        f'\nExpected: {new_gender}')


@pytest.mark.parametrize("current_gender", ["male", "female"], ids=['male_to_male', 'female_to_female'])
def test_change_old_gender(create_custom_human_gender_instance, current_gender):
    human = create_custom_human_gender_instance(current_gender)
    with pytest.raises(Exception):
        human.change_gender(current_gender)


@pytest.mark.parametrize("current_gender", ["male", "female"], ids=['male_to_wrong', 'female_to_wrong'])
def test_change_wrong_gender(create_custom_human_gender_instance, current_gender):
    human = create_custom_human_gender_instance(current_gender)
    wrong_gender = 'not_male'
    with pytest.raises(Exception):
        human.change_gender(wrong_gender)


@pytest.mark.skip(reason="bug - There is no gender check at creation")
def test_create_human_with_wrong_gender(create_custom_human_gender_instance):
    with pytest.raises(Exception):
        create_custom_human_gender_instance("wrong_gender")


@pytest.mark.parametrize("current_gender, new_gender", [("female", "male"), ("male", "female")],
                         ids=['female_to_male_died_human', 'male_to_female_died_human'])
def test_change_new_gender_to_died_human(create_custom_human_instance, current_gender, new_gender):
    human = create_custom_human_instance(100, current_gender)
    human.grow()
    with pytest.raises(Exception):
        human.change_gender(new_gender)


@pytest.mark.parametrize("gender", ["male", "female"], ids=['male_grow', 'female_grow'])
def test_correct_grow_up(create_custom_human_instance, gender):
    current_age = randint(1, 99)
    human = create_custom_human_instance(current_age, gender)
    human.grow()
    assert human.age == current_age + 1


@pytest.mark.parametrize("gender", ["male", "female"], ids=['male_die', 'female_die'])
def test_grow_up_human_die(create_custom_human_instance, gender):
    human = create_custom_human_instance(100, gender)
    human.grow()
    with pytest.raises(Exception):
        human.grow()
