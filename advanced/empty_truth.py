import random


def empty_truth(options=None):
    if not options:
        options = {'option1': 1}
    print(options)


def runs_before_function_called(opt: print('this runs'), arg=print('this also runs')) -> print('same here'):
    print("this doesn't print")


if __name__ == '__main__':

    x = (_ for _ in [])

    empty_truth()
    empty_truth(options={})
    print(random.randbytes(80).decode(errors='ignore'))

    print('-' * 20)

    # runs_before_function_called(opt=print('this also runs'), arg=print('this runs'))
    # print('-' * 20)

    print(0 or [] or {})
    print(0 or 1 or 2)
    print(1 and 2 and 3)
    print(1 and 0 and [])
