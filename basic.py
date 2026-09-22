# 1. Write a program to reverse a string without using a built-in reverse function. 
# 2. Write a program to check whether a given string or number is a palindrome. 
# 3. Write a program to find the largest and smallest elements in an array. 
# 4. Write a program to find duplicate elements in an array. 
# 5. Write a program to find the second-largest element in an array without sorting the array. 
# 6. Write a program to check whether a given number is prime.
# 7. Write a program to print the first N numbers of the Fibonacci series. 
# 8. Write a program to find the factorial of a given number using recursion. 
# 9. Write a program to check whether two given strings are anagrams of each other. 
# 10. Write a program to count the frequency of each character in a given string. 11. Write a program to find the missing number in an array containing numbers from 1 to N. 12. Given an array of integers and a target value, write a program to find two numbers whose sum equals the target value.


def rev(st):
    res = ""
    for i in st:
        res = i + res
    return res

print(rev("name"))

def if_palindrome(n):
    text = str(n).lower()
    return text == text[::-1]

print(if_palindrome("anna"))
print(if_palindrome(0))
print(if_palindrome("banana"))
print(if_palindrome(121))

def largest_smallest(num):
    large = num[0]
    small = num[0]
    for i in num:
        if i > large:
            large = i
        if i < small:
            small = i
    return large, small

print(largest_smallest([1,2,3,7,4,5]))

def duplicates(n):
    dups = []
    not_dups = []
    for i in n:
        if i not in not_dups:
            not_dups.append(i)
        elif i not in dups:
            dups.append(i)
    return dups, not_dups

print(duplicates([1,3,6,7,6,5,7,1,2,3,4]))

def second_largest(n):
    f = None
    s = None
    for i in n:
        if f is None:
            f = i
        elif s is None and i != f:
            if f < i:
                s = f
                f = i
            else:
                s = i
        elif i > f:
            s = f
            f = i
        elif s is not None and s < i and i != f:
            s = i
    return s

print(second_largest([-1, 2,5,56,34,99,200,45,29,-49]))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(15))

def fibonacci(n):
    seq = []
    a = 0
    b = 1
    for i in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

print(fibonacci(7))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

def is_anagrams(a, b):
    a = a.lower().replace(" ", "")
    b = b.lower().replace(" ", "")
    return sorted(a) == sorted(b)

print(is_anagrams("dormiTory", "dirty roOm"))

def counter(w):
    d = {}
    for i in w:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

print(counter("banana"))