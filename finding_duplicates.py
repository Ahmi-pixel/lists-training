def separate_duplicates(nums: list[int]) -> tuple[list[int], list[int]]:
    """Return (unique values in first-seen order, values that appeared more than once)."""
    o = []
    d = []

    for i in nums:
        if i in o:
            if i not in d:
                d.append(i)
        else:
            o.append(i)

    return o, d


if __name__ == "__main__":
    o, d = separate_duplicates([1, 0, 9, -9, 3, 4, 44, -44, 1])
    print(o)
    print(d)
