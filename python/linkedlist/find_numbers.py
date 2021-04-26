"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""
from typing import List


def find_numbers_matching_k(l: List, k: int):
    # O(n^2)
    # for i in l:
    #     for j in l:
    #         if i + j == k:
    #             return True
    # return False

    # O(n)
    s = set()
    for n in l:
        if k - n in s:
            return True
        else:
            s.add(n)
    return False

print(find_numbers_matching_k([10, 15, 3, 7], 17))
print(find_numbers_matching_k([10, 15, 3, 7], 20))


