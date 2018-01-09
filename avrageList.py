""" calculate avrage form list """

numbers = [0, 0, 0]


def avrageList(numbers):
    total = 0
    for i in numbers:
        total += i
    avrage = total / len(numbers)
    return avrage


print(avrageList(numbers))
