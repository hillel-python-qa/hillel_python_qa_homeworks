def getValue():
    result = input()

    try:
        result = int(result)
    except:
        print("Invalid value. Try again!")
        result = getValue()

    return result


def valueInversion(value):
    return value * -1


print("Enter any integer value: ")
value = getValue()
print(f"Original value: %d. Inverted value: %d" % (value, valueInversion(value)))
