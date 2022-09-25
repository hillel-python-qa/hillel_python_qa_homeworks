def contain_three():
    for index in range(0, 1000):
        if '3' in str(index):
            yield index


def contain_three_list_comp():
    return [item for item in range(0, 1000) if '3' in str(item)]


v1 = []
for index in contain_three():
    v1.append(index)
    print(index)

v2 = contain_three_list_comp()

print(v1 == v2)
