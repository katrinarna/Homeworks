
def fibonacci(length):
    a, b = 0, 1
    for _ in range(length):
        yield a
        a, b = b, a + b


