if __name__ == '__main__':
    with open("test/data/list_with_tuples.txt", "r") as file:
        elements = file.readlines()

output_of_results = []

for i in range(len(elements)):
    if elements[i][2] == "1":
        print(int(elements[i][0]) + int(elements[i][1]))
    elif elements[2] == "2":
        print(int(elements[i][0]) - int(elements[i][1]))
    elif elements[2] == "3":
        print(int(elements[i][0]) * int(elements[i][1]))
    else:
        print(int(elements[i][0]) / int(elements[i][1]))

print(output_of_results)
