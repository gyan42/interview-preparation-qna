"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of
all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
from typing import List
from itertools import product
from functools import reduce

def find_product(arr: List[int]):
    res = [1] * len(arr)
    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         if i != j:
    #             res[i] = res[i] * arr[j]

    prod = reduce(lambda x, y: x * y, arr)
    for i in range(len(arr)):
        # res[i] = int(prod / arr[i])
        res[i] = int(prod * pow(arr[i], -1))
    return res

print(find_product([1, 2, 3, 4, 5]))# == [120, 60, 40, 30, 24])
