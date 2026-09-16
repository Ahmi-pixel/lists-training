def find_target_brute(nums: list[int], target: int) -> list[tuple[int, int]]:
    """Method 1: check every pair. Returns (i, j) index pairs with i < j."""
    pairs = []
    for i, a in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if a + nums[j] == target:
                pairs.append((i, j))
    return pairs


def find_target(nums: list[int], target: int) -> list[tuple[int, int]]:
    """Method 2: one pass with a value -> index map. Returns (i, j) index pairs with i < j."""
    pairs = []
    d = {}

    for i, a in enumerate(nums):
        result = target - a
        if result in d:
            pairs.append((d[result], i))
        d[a] = i

    return pairs


if __name__ == "__main__":
    nums = [1, 7, 3, 2, 9]
    target = 9
    for i, j in find_target_brute(nums, target):
        print("Found", target, "at index:", i, j, "And their values are:", nums[i], nums[j])
    for i, j in find_target(nums, target):
        print(f"{target} found at indexes: {i} and {j} and their values are: {nums[i]} {nums[j]}")
