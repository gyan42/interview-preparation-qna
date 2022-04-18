from itertools import permutations, combinations

s = ['A','B','C']
print(f"Permuation of {s} is")
for p in permutations(s):
    print(p, end=" ")
print()
# ('A', 'B', 'C') ('A', 'C', 'B') ('B', 'A', 'C') ('B', 'C', 'A') ('C', 'A', 'B') ('C', 'B', 'A')

s = "ABC"
print(f"Combination of {s} is")
for i in range(len(s)+1):
    for c in combinations(s,i):
        print(c, end=" ")
print(" ")
# () ('A',) ('B',) ('C',) ('A', 'B') ('A', 'C') ('B', 'C') ('A', 'B', 'C')

#-----------------------------------------------------------------------------------------------------------------------

def permutate(s):
    if type(s) == str:
        s = list(s)
    res = []

    def swap(arr, i, j):
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t

    def _p(s, curr_index):
        if len(s) == curr_index:
            r = "".join(s)
            res.append(r)

        for i in range(curr_index, len(s)):
            swap(s, curr_index, i)
            _p(s, curr_index + 1)
            swap(s, curr_index, i)

    _p(s, 0)
    return res


print(" ".join(permutate(s)))


# Python function to print permutations of a given list
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l

print(" ".join(permutate(s)))

#----------------------------------------------------------------------------------------------------------------------
# TODO https://www.geeksforgeeks.org/recursive-program-to-generate-power-set/
def combination(s):
    pass


# Function to create combinations
# without itertools
def n_length_combo(lst, n):
    if n == 0:
        return [[]]

    l = []
    for i in range(0, len(lst)):
        m = lst[i]
        remLst = lst[i + 1:]

        for p in n_length_combo(remLst, n - 1):
            l.append([m] + p)

    return l

s = "abc"
print(f"Combination of {s} is")
for i in range(len(s)+1):
    for c in n_length_combo(s, i):
        print(c, end=" ")
print(" ")
# Driver code

#  ---------------------------------------------------------------------------------------------------------------------
from itertools import combinations
from collections import defaultdict

s = {15, 5, 20, 10, 35, 15, 10}
sum_cache = defaultdict(list)
for l in range(len(s)+1):
    for c in combinations(s, 1):
        print(c, end=" ")
        sum_cache[sum(c)].append(c)

print(sum_cache)