# making a digitalroot program.
# 15 should output 1 + 5 = 6

def digitalRoot(num):
    num = str(num)
    if len(num) == 1:
        return num
    else:
        counter = 0
        for i in num:
            counter += int(i)
        num = str(counter)
    return num


 # testing program

print(digitalRoot(100))
