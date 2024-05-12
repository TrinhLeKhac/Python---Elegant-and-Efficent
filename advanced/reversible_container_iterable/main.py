import collections.abc
import typing


class MyContainer:
    def __init__(self, l):
        self.l = l

    def __getitem__(self, item):
        return self.l[item]

    def __len__(self):
        return len(self.l)

    def __iter__(self):
        return iter(self.l)


class MyReversed:
    def __init__(self, seq):
        self.seq = seq
        self.n = len(seq) - 1
        if not hasattr(seq, '__getitem__'):
            raise TypeError("not reversible")

    def __iter__(self):
        return self

    def __next__(self):  # called by next()
        if self.n == -1:
            raise StopIteration
        n = self.n
        self.n = n - 1
        return self.seq[n]


def my_reversed(seq):
    n = len(seq) - 1
    if not hasattr(seq, '__getitem__'):
        raise TypeError("not reversible")
    while n != -1:
        yield seq[n]
        n -= 1


def reversed_example():
    print('>>> testing reversed')

    lst = [1, 2, 3, 4]

    print('Original reversed')
    for x in reversed(lst):
        print(x)

    print('My reversed func')
    for x in my_reversed(lst):
        print(x)

    print('My reversed class')
    my_rev = MyReversed(lst)
    for x in my_rev:
        print(x)


def container_example():

    print('>>> testing reversed with container')
    lst = [1, 2, 3, 4]
    container = MyContainer(lst)
    # print(f"{list(container)=}")
    list(container)

    print('Original reversed with my container')
    print(reversed(container))  # generator
    # print(reversed(reversed(l))) # ERROR

    print('My reversed func with my container')
    print(my_reversed(container))  # generator

    print('My reversed class with my container')
    my_rev = MyReversed(lst)
    print(my_rev)  # generator

    print('Exhausted reversed')
    lst = [1, 2, 3, 4]
    it = reversed(lst)
    print(list(it))
    print(list(it))

    print('Exhausted my reversed func')
    lst = [1, 2, 3, 4]
    it = my_reversed(lst)
    print(list(it))
    print(list(it))

    print('Exhausted my reversed class')
    lst = [1, 2, 3, 4]
    it = MyReversed(lst)
    print(list(it))
    print(list(it))


def copy_or_no_copy():
    print('>>> testing copy vs no_copy')
    lst = [("a", 1), ("b", 2), ("c", 3)]
    d = dict(lst)

    makes_a_copy = [
        dict(lst),
        frozenset(lst),
        list(lst),
        set(lst),
        sorted(lst),
        tuple(lst),
        lst[::-1],  # or any slice
        [x for x in lst],
    ]
    print('>>> make a copy')
    for x in makes_a_copy:
        print(x)

    doesnt_make_a_copy = [
        enumerate(lst),
        filter(None, lst),
        iter(lst),
        map(lambda x: x, lst),
        reversed(lst),
        zip(lst, lst),
        d.keys(),
        d.values(),
        d.items(),
        (x for x in lst),
    ]
    print(">>> doesn't make a copy")
    for x in doesnt_make_a_copy:
        print(x)


def numpy_example():
    print('>>> testing numpy')
    import numpy as np

    arr = np.array([1, 2, 3])
    rev = arr[::-1]

    print(arr)
    print(rev)

    print(arr.data)
    print(rev.data)

    print(arr.strides)
    print(rev.strides)


def sometimes_you_want_a_copy_example():
    d = {"a": 1, "b": 2, "c": 3}

    for char, val in list(d.items()):
        d[char.upper()] = val

    print(d)


def iterable_vs_Iterable():
    print('>>> testing iterable vs Iterable')
    container = MyContainer([1, 2, 3])
    print(isinstance(container, typing.Iterable))
    print(isinstance(container, collections.abc.Iterable))

    print(iter(container))
    # print(container.__iter__)


def main():
    reversed_example()
    container_example()
    print('-'*20)
    copy_or_no_copy()
    numpy_example()
    sometimes_you_want_a_copy_example()
    print('-'*20)
    iterable_vs_Iterable()


if __name__ == '__main__':
    main()
