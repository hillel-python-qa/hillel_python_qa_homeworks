def custom_all(collection: iter) -> iter:
    for element in collection:
        if not bool(element):
            return False
    return True


all_true = [True, True, True, True, True]
with_false = [True, True, True, True, False]
print(custom_all(all_true))
print(custom_all(with_false))
