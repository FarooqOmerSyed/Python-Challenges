def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    fib_prev, fib_curr = 0, 1
    for i in range(2, n):
        fib_next = fib_prev + fib_curr
        fib_prev, fib_curr = fib_curr, fib_next

    return fib_curr


print(fibonacci(10))
