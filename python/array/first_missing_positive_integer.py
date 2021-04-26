"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
def fin_min_positive_num(lst):
    sorted_list = sorted(lst) # O(log N)
    print(sorted_list)
    for i in range(len(sorted_list)-1): # O(N)
        if sorted_list[i+1] - abs(sorted_list[i]) == 1 or sorted_list[i+1] - abs(sorted_list[i]) == 0:
            continue
        else:
            return sorted_list[i] + 1
    return sorted_list[-1] + 1

print(fin_min_positive_num([3, 4, -1, 1]))
print(fin_min_positive_num([1, 2, 0]))