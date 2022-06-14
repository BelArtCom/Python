def get_factorial_num(index):
    if index == 0:
        return 0
    
    if index == 1:
        return 1

    return get_factorial_num(index - 1) + get_factorial_num(index - 2)

def get_factorial_num(index):
    if index == 0:
        return 1
    
    if index == 1:
        return 1

    return index * get_factorial_num(index - 1)