# The bisect left function returns the index of the sorted list
# where the element should be added to maintain the list in order.
# If the element already exists in the list, bisect left will return the index of the element's first occurrence.

# In contrast, the bisect right function returns the rightmost index in the sorted list where the element should be put.
# If the element is already present in the list,
# bisect_right will return the next index after the last occurrence of the element

# from bisect import bisect_left, bisect_right

def bisect_left(arr: list, x) -> int:
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_right(arr: list, x) -> list:
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > x:
            hi = mid
        else:
            lo = mid + 1
    return lo


def test_bisections():
    assert bisect_left([], 0) == 0
    assert bisect_right([], 0) == 0
    assert bisect_left([0], 0) == 0
    assert bisect_right([0], 0) == 1
    assert bisect_left([0, 0, 0], 0) == 0
    assert bisect_right([0, 0, 0], 0) == 3
    assert bisect_left([2, 3, 3, 4, 6, 7, 8, 9], 7) == 5
    assert bisect_right([2, 3, 3, 4, 6, 7, 8, 9], 7) == 6
    assert bisect_left([2, 3, 3, 4, 6, 8, 9], 7) == 5
    assert bisect_right([2, 3, 3, 4, 6, 8, 9], 7) == 5


if __name__ == '__main__':
    test_bisections()

