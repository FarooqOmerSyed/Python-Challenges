def fibonacci(n):
    fibo_seq = [0, 1]

    while len(fibo_seq) < n:
        fib_next = fibo_seq[-1] + fibo_seq[-2]
        fibo_seq.append(fib_next)

    return fibo_seq


print(fibonacci(10))