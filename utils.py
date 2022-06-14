def get_fibonacci_num(fibonacci):
    fib_list = [0, 1]
    for i in range(1, fibonacci):
        fib_list_0 = fib_list[0]
        fib_list_1 = fib_list[1]
        fib_list[0] = fib_list_1
        fib_list[1] = fib_list_0 + fib_list_1
    return fib_list[1]
