"""
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
"""

from itertools import permutations

# for e in permutations({1,2,3}):
#     print(e)
#
from itertools import combinations

s = {1,2,3}
for i in range(len(s)+1):
    for e in combinations(s, i):
        print(e, end=" ")