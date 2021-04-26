"""
 return a new sorted merged list from K sorted lists, each with size N.
"""
from functools import reduce
flat_map = lambda f, xs: reduce(lambda a, b: a + b, map(f, xs))

# O(KN log KN)
def merge_lists(lists):
    # flattend_list = []
    # for l in lists:
    #     flattend_list.extend(l)
    flattend_list = flat_map(lambda x: x, lists)
    return sorted(flattend_list)

print(merge_lists([[10, 15, 30], [12, 15, 20], [17, 20, 32]]))
# [10, 15, 30, 12, 15, 20, 17, 20, 32]

# print(reduce(lambda a, b :  a + b, [1,2,3,4,5]))

import heapq

# O(KN log K)
def merge(lists):
    print(lists)
    merged_list = []
    # (val, list_index, element_index)
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    print(heap)
    heapq.heapify(heap)
    print(heap)


    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)

        merged_list.append(val)

        # Let's say the smallest element is E. Once we get E, we know we're interested in only
        # the next element of the list that held E. Then we'd extract out the second smallest element and etc.
        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
            print(heap)
    return merged_list

print("*" * 100)
print(merge([[10, 15, 30, 31], [12, 15, 20, 21], [17, 20, 32, 33], [1, 2, 3, 4]]))
# [1, 2, 3, 4, 10, 12, 15, 15, 17, 20, 20, 21, 30, 31, 32, 33]