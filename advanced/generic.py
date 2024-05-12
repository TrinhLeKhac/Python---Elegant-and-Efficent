from types import GenericAlias
from typing import List, TypeVar

if __name__ == '__main__':
    # List
    X: List[int] = []

    # list
    x: list[int] = []

    xx = list[int]()

    xxx = []

    print('type:', type(X))
    print('type:', type(x))
    print('type:', type(xx))

    print('compare:', List[int] == list[int])
    print('-'*20)

    # origin and args
    print('print:', list[int])  # __repr__
    print('origin:', list[int].__origin__)
    print('arg:', list[int].__args__)
    print('-'*20)

    print('arg:', dict[str, int].__origin__)
    print('arg:', dict[str, int].__args__)
    print('-' * 20)

    # parameters
    T = TypeVar('T')
    print('print:', T)
    print('print:', dict[str, T])
    print('origin:', dict[str, T].__origin__)
    print('args:', dict[str, T].__args__)
    print('parameters:', dict[str, T].__parameters__)
    print('-' * 20)

    # comparing types
    # print(isinstance([1, 2, 3], list[int]))  # Parameterized generics cannot be used with instance and class checks
    # print(issubclass(list, list[int]))  # Parameterized generics cannot be used with instance and class checks
    print(isinstance(list[int], GenericAlias))
