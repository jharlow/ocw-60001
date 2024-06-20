fib_2_count: int = 0


def fib(n: int) -> int:
    global fib_2_count
    if n == 2:
        fib_2_count += 1
    return 1 if n <= 1 else fib(n - 1) + fib(n - 2)


fib(5)
print(fib_2_count)
