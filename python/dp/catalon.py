"""
The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …


Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.

    Count the number of expressions containing n pairs of parentheses which are correctly matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
    Count the number of possible Binary Search Trees with n keys (See this)
    Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.
    Given a number n, return the number of ways you can draw n chords in a circle with 2 x n points such that no 2 chords intersect.


C_0 = 1
C_1 = 1
sum(C_i * C_n-i-1)_i{0,n} for n > 0
"""

def catalon(n):
    if n <= 1:
        return 1

    res = 0
    for i in range(n):
        res += catalon(i) * catalon(n-i-1)

    return res

for i in range(10):
    print(catalon(i), end=" ")


def catalondp(n):
    if n <= 1:
        return 1
    cache = [0] * (n)
    cache[0] = 1
    cache[1] = 1

    for i in range(2, n):
        for j in range(i):
            cache[i] += cache[j] * cache[i-j-1]
    return cache

print(catalondp(10))
