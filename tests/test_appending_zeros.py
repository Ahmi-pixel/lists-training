from appending_zeros import move_zeros_front


def test_basic():
    assert move_zeros_front([99, 60, 0, 0, 7, 7, 70, 2, 0, 1, 10]) == [0, 0, 0, 99, 60, 7, 7, 70, 2, 1, 10]


def test_preserves_order_of_non_zeros():
    assert move_zeros_front([3, 0, 1, 0, 2]) == [0, 0, 3, 1, 2]


def test_no_zeros():
    assert move_zeros_front([1, 2, 3]) == [1, 2, 3]


def test_all_zeros():
    assert move_zeros_front([0, 0, 0]) == [0, 0, 0]


def test_empty():
    assert move_zeros_front([]) == []
