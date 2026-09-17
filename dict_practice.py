# 1. Count character frequency

text = "banannna"
d = {}

for i in text:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
# Output: {'b': 1, 'a': 3, 'n': 2}

# 2. Find the key with the highest value

scores = {
     "Ali": 85,
     "John": 92,
     "Sara": 88
}
best_name = None
best_score = 0       # (a) a number so low that any real score beats it

for key, values in scores.items():
    if values > best_score:      # (b) the comparison: is this score better than the best so far?
        best_score = values
        best_name = key           # (c) which variable holds the name that goes with `values`?

print(best_name)

# Output: "John"

# 3. Find common elements between two sets

# Method: 1
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a & b
print(c)

# Method: 2
common = set()

for i in a:
    if i in b:
        common.add(i)
print(common)
# Output: {3, 4}

# 4. Tuple immutability trap

x = ([1, 2], [3, 4])
x[0].append(5)

print(x)
# Question: If tuples are immutable, why does this work?
# Because technically we are not mutating the tuple, we are mutating the list inside the tuple

# 5. Dictionary key trap
# data = {
#     (1, [2]): "hello"
# }
# Question: What happens, and why can't a list be a dictionary key?

# Answer: We get an exception Typeerror. We can not use list as keys because keys are hashable objects and lists are unhashable

# 6. List of tuples to Dictionary
data = [
    ("Ali", 25),
    ("Sara", 30),
    ("John", 28)
]
# Question: Convert this into:
# {
#     "Ali": 25,
#     "Sara": 30,
#     "John": 28
# }

d = {}

for i,a in enumerate(data):
    if a not in d:
        i = a[0]
        d[i] = a[1] 
        print(a,d)  
print(d)

