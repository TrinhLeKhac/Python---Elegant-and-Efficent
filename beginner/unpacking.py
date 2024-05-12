def numbers(a, b, c, d):
    print(a, b, c, d)


lst = [1, 2, 3, 4]
print(numbers(lst[0], lst[1], lst[2], lst[3]))
print(numbers(*lst))

values = {
    "key": 5,
    "target": 10,
}


def parse_values(key, target):
    print(key, target)


parse_values(**values)  # key=5, target=10
