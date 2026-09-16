def second_highest(nums: list[int]) -> int | None:
    """Return the second largest distinct value, or None if there isn't one."""
    first = None
    second = None

    for n in nums:
        if first is None:
            first = n
        elif second is None and n != first:
            if first < n:
                second = first
                first = n
            else:
                second = n
        elif n > first:
            second = first
            first = n
        elif second is not None and second < n and n != first:
            second = n

    return second


if __name__ == "__main__":
    result = second_highest([-1, -2, 9, 3, 44, -95, 0, 3, 20])
    print(result, "is the second largest number.")
