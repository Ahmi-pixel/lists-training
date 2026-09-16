import pytest

from find_target import find_target, find_target_brute


@pytest.mark.parametrize("fn", [find_target, find_target_brute])
def test_basic(fn):
    assert fn([1, 7, 3, 2, 9], 9) == [(1, 3)]


@pytest.mark.parametrize("fn", [find_target, find_target_brute])
def test_no_match(fn):
    assert fn([1, 2, 3], 100) == []


@pytest.mark.parametrize("fn", [find_target, find_target_brute])
def test_does_not_pair_element_with_itself(fn):
    assert fn([4, 1], 8) == []


@pytest.mark.parametrize("fn", [find_target, find_target_brute])
def test_multiple_pairs(fn):
    assert sorted(fn([1, 5, 3, 3, 5], 6)) == [(0, 1), (0, 4), (2, 3)]


@pytest.mark.parametrize("fn", [find_target, find_target_brute])
def test_empty(fn):
    assert fn([], 0) == []
