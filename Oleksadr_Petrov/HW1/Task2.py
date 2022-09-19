def getCount():

    result = input()

    try:
        result = int(result)
    except:
        print("Not a integer. Try again!")
        result = getCount()

    if result <= 0:
        print("Invalid value. Try again!")
        result = getCount()

    return result


def applesDivision(students, apples):

    applesForEachStudent = apples // students
    applesInBasket = apples % students
    return [applesForEachStudent, applesInBasket]


print("Enter the students count: ")
students = getCount()
print("Enter the apples count: ")
apples = getCount()
result = applesDivision(students, apples)
print(f"Apples for each student: %d. Apples in basket: %d" % (result[0], result[1]))
