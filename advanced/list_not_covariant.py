class Base:
    def do_something(self):
        pass


class Derived(Base):
    def do_something_else(self):
        pass


def append_base(l: list[Base]):
    l.append(Base())


def main():
    l: list[Derived] = [Derived()]
    append_base(l)
    print(l)
    for derived in l:
        derived.do_something_else()
        # AttributeError: 'Base' object has no attribute 'do_something_else'. Did you mean: 'do_something'?


if __name__ == '__main__':
    main()
