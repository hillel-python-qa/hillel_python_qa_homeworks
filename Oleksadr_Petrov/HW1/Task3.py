def getValue():

    result = input()

    try:
        result = int(result)
    except:
        print("Invalid value. Try again!")
        result = getValue()

    return result


def nearestValuesCalc(value):

    prevValue = value - 1
    nextValue = value + 1
    return [prevValue, nextValue]


print("Enter any integer value: ")
value = getValue()
result = nearestValuesCalc(value)
print(f"Previous value: %d. Next value: %d" % (result[0], result[1]))
