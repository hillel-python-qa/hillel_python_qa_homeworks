import pytest


def test_human_instance(create_custom_human):
    name = 'Bella'
    age = 43
    gender = 'female'
    dummy = create_custom_human(name, age, gender)
    assert dummy._Human__name == name, f'Name is: {dummy._Human__name}. While expected name is: {name}'
    assert dummy.age == age, f'Age is: {dummy.age}. While expected age is: {age}'
    assert dummy.gender == gender, f'gender is:{dummy.gender}. While expected gender is: {gender}'


def test_growth(create_custom_human):
    jonny_age = 35
    dummy = create_custom_human('Jonny', jonny_age, 'male')
    dummy.grow()
    assert dummy.age == jonny_age + 1, (f"Function grow() haven't been executed properly"
                                        f"AR: {dummy.age}"
                                        f"ER: 36")


def test_death(create_custom_human):
    dummy = create_custom_human('Old_Jonny', 100, 'male')
    dummy.grow()
    assert dummy._Human__status == 'dead', f'{dummy._Human__name} should be dead, as their age reached past 100'


def test_gender_change_valid(create_custom_human):
    dummy = create_custom_human('Random_Citizen', 25, 'male')
    dummy.change_gender('female')
    assert dummy.gender == 'female', f"ER: {dummy._Human__name}'s gender should be 'female" \
                                     f"AR: the gender is '{dummy.gender}'"


@pytest.mark.parametrize('gender', ['fefefe', 11])
def test_gender_change_invalid(create_custom_human, gender):
    dummy = create_custom_human('Kriss', 33, 'female')
    with pytest.raises(Exception, match="Not correct name of gender"):
        dummy.change_gender(gender)


def test_gender_change_same(create_custom_human):
    dummy = create_custom_human('Tomura', 53, 'male')
    with pytest.raises(Exception):
        dummy.change_gender('male')


def test_gender_change_in_dead(create_custom_human):
    dummy = create_custom_human('Albert', 100, 'male')
    dummy.grow()
    with pytest.raises(Exception):
        dummy.change_gender('Female')
