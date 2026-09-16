def three_sum(nums: list[int]) -> list[list[int]]:
    """Return all unique triplets that sum to zero, each sorted ascending."""
    n = sorted(nums)
    res = []
    for i, a in enumerate(n):
        if i > 0 and a == n[i-1]:
            continue
        l, r = i + 1, len(n) - 1
        while l < r:
            s = a + n[l] + n[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([a, n[l], n[r]])
                l += 1
                while l < r and n[l] == n[l - 1]:
                    l += 1
    return res


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))
