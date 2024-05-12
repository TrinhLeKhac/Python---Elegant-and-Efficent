from typing import TypeVar

T = TypeVar('T', str, bytes, bytearray)  # Must be exactly str or bytes or bytearray


def remove_prefix(s: T, prefix: T) -> T:
    if s.startswith(prefix):
        return s[len(prefix):]
    else:
        return s[:]


def remove_suffix(s: T, suffix: T) -> T:
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    else:
        return s[:]


def test_remove_prefix():
    assert remove_prefix('abctest', 'abc') == 'test'
    assert remove_prefix('abctest', 'def') == 'abctest'
    assert remove_prefix('abctest', '') == 'abctest'
    assert remove_prefix('', 'def') == ''
    assert remove_prefix('', '') == ''

    assert remove_prefix(b'abctest', b'abc') == b'test'
    assert remove_prefix(b'abctest', b'def') == b'abctest'
    assert remove_prefix(b'abctest', b'') == b'abctest'
    assert remove_prefix(b'', b'def') == b''
    assert remove_prefix(b'', b'') == b''

    assert remove_prefix(bytearray(b'abctest'), bytearray(b'abc')) == bytearray(b'test')
    assert remove_prefix(bytearray(b'abctest'), bytearray(b'def')) == bytearray(b'abctest')
    assert remove_prefix(bytearray(b'abctest'), bytearray(b'')) == bytearray(b'abctest')
    assert remove_prefix(bytearray(b''), bytearray(b'def')) == bytearray(b'')
    assert remove_prefix(bytearray(b''), bytearray(b'')) == bytearray(b'')

    x = bytearray(b'123')
    y = remove_prefix(x, bytearray(b'abc'))
    assert y == x
    assert y is not x

    print('passed')


if __name__ == '__main__':

    # remove_suffix files example
    files: list[str] = ['paint.exe', 'word.exe', 'virus.exe', 'not-modified-example']
    files_removed = [remove_suffix(x, '.exe') for x in files]
    print(files)
    print(files_removed)

    # bytes Response example
    print(b'Response: DATA'.removeprefix(b'Response: '))

    # NOT rstrip and lstrip
    files = [x.rstrip('.exe') for x in files]
    print(files)

    # sample implementation, tests first!
    test_remove_prefix()

    #  Both byte and bytearray are arrays of bytes with values ranging from 0 to 255
    print(b'xyz')  # byte immutable
    print(bytearray(b'xyz'))  # bytearray mutable
