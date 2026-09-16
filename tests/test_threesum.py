from threesum import three_sum


def test_basic():
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]


def test_no_triplets():
    assert three_sum([1, 2, 3]) == []


def test_all_zeros_gives_one_triplet():
    assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]


def test_does_not_mutate_input():
    nums = [3, -1, -2]
    three_sum(nums)
    assert nums == [3, -1, -2]


def test_empty():
    assert three_sum([]) == []
