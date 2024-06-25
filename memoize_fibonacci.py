cache = {}


def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 1:  # Change the condition to n <= 1 to handle cases where n is 0 or 1
        return n
    result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result
    return result


print(fibonacci(10))  # 55
print(fibonacci(15))  # 610
