def divisible_by_seven_gen():
    for index in range(0, 1000):
        if index % 7 == 0:
            yield index


def divisible_by_seven_gen_v2():
    for index in range(0, 1000, 7):
        yield index


def divisible_by_seven_list_comp():
    return [item for item in range(0, 1000, 7)]


v1 = []
for index in divisible_by_seven_gen():
    v1.append(index)
    print(index)

v2 = []
for index in divisible_by_seven_gen_v2():
    v2.append(index)
    print(index)

v3 = divisible_by_seven_list_comp()

print(v1 == v2)
print(v2 == v3)
