# binary in list
# regular converter besides the binary is in form of a list. 

liste = [0, 1, 0, 1]


def binary(liste):
    number = 0
    counter = 0
    # iterate in reverse
    for i in liste[::-1]:
        number += i * (2**counter)
        counter += 1

    return number


print(binary(liste))
