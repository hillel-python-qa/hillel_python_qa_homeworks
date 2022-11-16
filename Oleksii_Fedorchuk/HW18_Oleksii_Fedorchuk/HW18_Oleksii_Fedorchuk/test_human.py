from human import Human


def dead_test():
    age = Human.age
    age = 80
    limit = Human.grow
    assert age == limit


