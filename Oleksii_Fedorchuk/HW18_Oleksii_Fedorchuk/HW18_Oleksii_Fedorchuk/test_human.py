import pytest


def test_human_creating(human_template):
    """
    Pre-Condition:
    create_human texture is created
    Steps:
    1. Add name
    2. Add age
    3. Add gender
    ER: [Human is created]
    """
    human = human_template("Harry", 12, "male")
    assert human._Human__name == "Harry"
    assert human.age == 12
    assert human.gender == "male"


@pytest.mark.xfail
@pytest.mark.parametrize("name, age, gender", [("Harry", -10, "male")])
def test_human_negative_age(human_template, name, age, gender):
    """
    Pre-Condition:
    create_human texture is created
    Steps:
    1. Add name
    2. Add incorrect age
    3. Add gender
    ER: Human age test should be fell, the age cannot be negative
    """
    human = human_template(name, age, gender)
    assert human.age >= 0, f"Human age cannot be less then 0"


@pytest.mark.parametrize("name, age, gender", [("Harry", 12, "male"), ("Hermione", 11, "female")])
def test_human_gender(human_template, name, age, gender):
    """
    Pre-Condition:
    create_human texture is created
    Steps:
    1. Add name
    2. Add age
    3. Add gender
    ER: Human should have gender
    """
    human = human_template(name, age, gender)
    assert human.gender == gender, f"Human gender is {gender}"


def test_human_change_gender(human_template):
    """
    Pre-Condition:
    create_human texture is created
    Steps:
    1. Add name
    2. Add age
    3. Add gender
    4. Add invalid gender
    ER: Human should have gender
    """
    human = human_template("Name", 15, "male")
    with pytest.raises(Exception, match="Not correct name of gender"):
        human.change_gender("femalee")


def test_human_same_gender(human_template):
    """
    Pre-Condition:
    create_human texture is created
    Steps:
    1. Add name
    2. Add age
    3. Add the same gender
    4. Add invalid gender
    ER: Human should have "already has gender" status
    """
    human = human_template("Hermione", 12, "female")
    with pytest.raises(Exception, match=f"{human._Human__name} already has gender '{human.gender}'"):
        human.change_gender("female")


def test_human_grow(human_template):
    """
        Pre-Condition:
        "create_human" texture is created
        Steps:
        1. Add name
        2. Add age
        3. Add gender
        4. Add valid gender
        5. Add one more year by grow func
        ER: Human should get one year older
        """
    current_age = 12
    human = human_template("Harry", current_age, "male")
    human.grow()
    assert human.age == current_age + 1


def test_dead_human_(human_template):
    """
    Pre-Condition:
    create_human texture is created
    Steps:
    1. Add name
    2. Add invalid age
    3. Add gender
    ER: Human status should be "dead"
    """
    human = human_template("Name", 200, "male")
    human.grow()
    assert human._Human__status == "dead"
