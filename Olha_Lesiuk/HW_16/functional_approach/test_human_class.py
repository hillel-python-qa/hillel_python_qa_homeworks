from hillel_python_qa_homeworks.Olha_Lesiuk.HW_16.human import Human


def test_alive_or_dead():
    age = Human
    new_age = 54
    age.grow = 54
    assert age.grow, (f'A man is dead'
                      f'\nActual: {age.grow}'
                      f'\nExpected: {new_age}')
