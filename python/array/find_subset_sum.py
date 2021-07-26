"""
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into
{15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.

https://www.geeksforgeeks.org/partition-problem-dp-18/
https://www.youtube.com/watch?v=obhWqDfzwQQ
"""

# bottom up aprroach
#
def is_subset_exists(arr, n, s, cache, pos):
    """
    arr and n is passed as it is
    pos and sum varies between two sets : s1 and s2
    Args:
        arr:
        n:
        s:
        cache:
        pos:

    Returns:

    """
    if s == 0:
        return True
    if pos >= n or s < 0:
        return False

    # if arr[n-1] > s:
    #     return is_subset_exists(arr, n-1, s)

    if cache[n][s] != -1:
        return cache[n][s]

    # Each element can only be in set1 or set2
    # An element is included in the set by removing the value form the sum
    cache[n][s] = is_subset_exists(arr, n, s, cache, pos+1) or is_subset_exists(arr, n, s-arr[pos], cache, pos+1)
    return cache[n][s]

"""
We can split into two sets only when the sum is even
x + x => 2x or 2x%2 == 0
"""
def can_split(arr):
    s = sum(arr)
    n = len(arr)
    if s % 2 != 0:
        return False
    # l rows sum/2 columns
    cache= [[-1] * int((s // 2)+1)] * int(n+1)

    ret = is_subset_exists(arr, n, s//2, cache, 0)
    print(cache)
    return ret



print(can_split([15, 5, 20, 10, 35, 15, 10]))
print(can_split({15, 5, 20, 10, 35}))

