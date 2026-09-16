from second_highest import second_highest


def test_basic():
    assert second_highest([-1, -2, 9, 3, 44, -95, 0, 3, 20]) == 20


def test_ascending():
    assert second_highest([1, 2, 3, 4]) == 3


def test_descending():
    assert second_highest([4, 3, 2, 1]) == 3


def test_ignores_repeated_max():
    assert second_highest([5, 5, 3]) == 3


def test_all_negative():
    assert second_highest([-10, -3, -7]) == -7


def test_all_same_returns_none():
    assert second_highest([7, 7, 7]) is None


def test_single_element_returns_none():
    assert second_highest([1]) is None


def test_empty_returns_none():
    assert second_highest([]) is None
