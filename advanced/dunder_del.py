import json
import shutil
import tempfile
import weakref


class A:
    def __del__(self):
        print("cleanup code?")


class DumpOnDel:
    def __del__(self):
        with open("out.json", "w") as f:
            json.dump("test", f)  # what is json no longer exists?


def plain_del_example():
    print("start")
    x = A()
    # y = x
    del x
    print("stop")


class B:
    def __del__(self):
        print(f"{self.__class__.__name__}.__del__")
        raise ValueError


def del_ignores_exceptions():
    print("start")
    x = B()
    del x
    print("stop")


def del_may_never_be_called():
    x = A()
    y = A()
    x.children = [y]
    y.parent = x

    try:
        raise ValueError
    except ValueError as exc:  # always causes a cycle
        print(exc.__traceback__.tb_frame.f_locals['exc'] is exc)


global_x = None


class Bad:
    def __del__(self):
        global global_x
        print(f"{self.__class__.__name__}.__del__")
        global_x = self


def del_may_be_called_multiple_times():
    x = Bad()
    print(x)
    del x

    global global_x
    print(global_x)  # "resurrected"
    del global_x
    # del not called again, impl detail


# https://docs.python.org/3/library/weakref.html?highlight=__weakref__#comparing-finalizers-with-del-methods
class TempDir:
    def __init__(self):
        self.name = tempfile.mkdtemp()
        self._finalizer = weakref.finalize(self, shutil.rmtree, self.name)

    def remove(self):
        self._finalizer()

    @property
    def removed(self):
        return not self._finalizer.alive

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.remove()


def best_del_alternative():
    with TempDir() as d:
        ...
    assert d.removed


def main():
    print('>>> Plain del example: ')
    plain_del_example()
    print('-'*20)

    print('>>> Del ignores exceptions')
    del_ignores_exceptions()
    print('-'*20)

    print('>>> Del may never be called')
    del_may_never_be_called()
    print('-'*20)

    print('>>> Del may be called multiple times')
    del_may_be_called_multiple_times()
    print('-'*20)

    print('>>> Best del alternative')
    best_del_alternative()
    print('-'*20)


if __name__ == '__main__':
    main()
