def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    if n == 0:
        return 0  # Directly return the first Fibonacci number
    if n == 1:
        return 1  # Directly return the second Fibonacci number

    # Recursive calls for the two preceding numbers
    return fibonacci(n-1) + fibonacci(n-2)

