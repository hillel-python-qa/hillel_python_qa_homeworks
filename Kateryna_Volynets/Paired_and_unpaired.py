numbers = [1, 2, 3, 4, 5, 6, 7, 8]
paired_value, unpaired_value = [], []
paired_index, unpaired_index = [], []
for index, i in enumerate(numbers):
    if index % 2 == 1:
        unpaired_index.append(index)
        unpaired_value.append(i)
    else:
        paired_index.append(index)
        paired_value.append(i)

list_paired = zip(paired_index, paired_value)
list_unpaired = zip(unpaired_index, unpaired_value)
print(list(list_unpaired))
print(list(list_paired))
