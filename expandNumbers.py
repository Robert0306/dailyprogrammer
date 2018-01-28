# script to find the expanded number form.


def expandedNumber(num):
    answer = []
    divide = 10
    # using 10 to divide the int.
    while divide < num:
        # modulo helps us find the number we need to work with.
        rest = num % divide
        if rest != 0:
            answer.insert(0, str(rest))
            # Then we need to decrement num to find another number to work with
        num -= rest
        divide = divide * 10
    answer.insert(0, str(num))
    return "+".join(answer)

# should ofc have more tests.
print(expandedNumber(12))
