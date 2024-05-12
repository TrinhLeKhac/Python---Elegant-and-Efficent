import functools


def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]

    if n == 0:
        return 0
    if n == 1:
        return 1

    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]


@functools.cache
def fibonacci_with_cache(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_with_cache(n - 1) + fibonacci_with_cache(n - 2)


print(fibonacci(40))
print(fibonacci_with_cache(40))
