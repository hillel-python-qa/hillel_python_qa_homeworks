def getCathetus():

    result = input()

    try:
        result = float(result)
    except:
        print("Not a number. Try again!")
        result = getCathetus()

    if result <= 0:
        print("Invalid value. Try again!")
        result = getCathetus()

    return result


def triangleArea(c1, c2):

    result = 0.5 * c1 * c2
    return result


print("Enter the first cathetus: ")
firstCathetus = getCathetus()
print("Enter the second cathetus: ")
secondCathetus = getCathetus()
print("Triangles area: ", triangleArea(firstCathetus, secondCathetus))