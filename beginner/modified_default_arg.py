def func(lst=None):
    if lst is None:
        lst = [1, 2]
    lst.append(100)
    return lst


def func_mutable(lst=[1, 2]):  # default argument is mutable
    lst.append(100)
    return lst


lst1 = func()
lst2 = func()
lst3 = func()
print(lst1, lst2, lst3)

# don't use multable as default argument
lst4 = func_mutable()  # modified default argument
lst5 = func_mutable()
lst6 = func_mutable()
print(lst4, lst5, lst6)

generator = (i for i in range(5))
print(generator)

sentences = "hello my name is trinhlk2"
char_dict = {char: sentences.count(char) for char in set(sentences)}
print(char_dict)

ternary = 1 if 2 > 4 else 0  # inline/ternary condition
print(ternary)

lst_demo = [[1, 2], [3, 4], [4, 2], [-1, 3], [4, 5], [2, 3]]


def sort_func(x):
    return x[0] + x[1]


lst_demo.sort(key=sort_func, reverse=True)  # inplace replace
lst_demo.sort(key=lambda x: x[0], reverse=True)
lst_demo.sort()
sorted(lst_demo)
print(lst_demo.sort())  # None
print(lst_demo)
