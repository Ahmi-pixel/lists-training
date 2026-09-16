def move_zeros_front(nums: list[int]) -> list[int]:
    zero = []
    new = []

    for i in nums:
        if i == 0:
            zero.append(i)
        else:
            new.append(i)

    return zero + new


if __name__ == "__main__":
    print(move_zeros_front([99, 60, 0, 0, 7, 7, 70, 2, 0, 1, 10]))
