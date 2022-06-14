def get_fibonacci_num(index):
    if index == 0:
        return 0

    if index == 1:
        return 1

    first = 0
    second = 1
    for i in range(1, index):
        sum = first + second
        first = second
        second = sum

    return sum


def get_factorial_num(index):
    if index == 0:
        return 1
    
    if index == 1:
        return 1

    result = 1
    for i in range(1, index + 1):
        result *= i
    
    return result