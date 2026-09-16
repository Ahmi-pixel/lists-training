from list_tuple import func1, func


def test_sorted_descending():
    assert func1([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


def test_sorted_descending_unsorted_input():
    assert func1([1, 2, 3, 4, 5, 2]) == [5, 4, 3, 2, 2, 1]


def test_does_not_mutate_input():
    nums = [3, 1, 2]
    func1(nums)
    assert nums == [3, 1, 2]


def test_missing_number():
    assert func([1, 2, 3, 5, 6], 6) == 4


def test_missing_number_none_missing():
    assert func([1, 2, 3], 3) == 0

