from finding_duplicates import separate_duplicates


def test_basic():
    unique, dups = separate_duplicates([1, 0, 9, -9, 3, 4, 44, -44, 1])
    assert unique == [1, 0, 9, -9, 3, 4, 44, -44]
    assert dups == [1]


def test_no_duplicates():
    assert separate_duplicates([1, 2, 3]) == ([1, 2, 3], [])


def test_value_seen_three_times_listed_once():
    unique, dups = separate_duplicates([5, 5, 5, 2])
    assert unique == [5, 2]
    assert dups == [5]


def test_multiple_duplicates_in_first_seen_order():
    _, dups = separate_duplicates([2, 1, 1, 2, 3])
    assert dups == [1, 2]


def test_empty():
    assert separate_duplicates([]) == ([], [])
