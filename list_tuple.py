# Question: 1
def func1(n):
    clean = sorted(n)
    num = clean[::-1]
    return num

print(func1([1, 2, 3, 4, 5, 2]))

# Question: 2
# x = (1, 2, 3)
# x[0] = 10

# Can not mutate tuple

# Question: 3
def func(num, n):
    expected = n * (n + 1) // 2

    actual = sum(num)

    return expected - actual

print(func([1, 2, 3, 5, 6], 6))

# Question: 4
data = (10, (20, 30), 40)

print(data[1][1])