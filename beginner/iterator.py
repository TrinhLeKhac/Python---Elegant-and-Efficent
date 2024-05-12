import sys

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sys.getsizeof(lst))
print(sys.getsizeof(range(1, 11)))

y = map(lambda x: x ** 2, lst)
print(type(y))  # iterator
print(sys.getsizeof(y))

next(y)
print(next(y))
print(next(y))
for item in y:
    print(item)

while True:
    try:
        value = next(y)
        print(value)
    except StopIteration:
        print('Done')
        break


class Iter:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.n:
            raise StopIteration
        return self.current


demo_iter = Iter(5)
for i in demo_iter:
    print(i)
