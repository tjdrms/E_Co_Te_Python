def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n-1)

print('재귀적으로 구현', factorial(6))
