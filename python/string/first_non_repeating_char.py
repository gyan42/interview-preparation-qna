import sys
s = "mageswaran"
##store the first occurance index and find minimum of those all
def first_non_repeating_char_index(s):
    NUM_CHARS = 256
    arr = [-1 for i in range(NUM_CHARS)] # init with -1

    for i in range(len(s)):
        c = s[i]
        if arr[ord(c)] == -1: #1st occurance
            arr[ord(c)] = i
        else:
            arr[ord(c)] == -2

    # Regardless of the length of the input string, the indexes are reduced to 256 chars
    min_index = sys.maxsize
    for i in arr:
        if i >= 0:
            min_index = min(i, min_index)
#     print(min_index)
    return min_index


i = first_non_repeating_char_index(s)
print(s[i])


print("===============================================================================================================")
from collections import Counter
def first_non_repeating_char_index(s):
    counter = Counter(s)

    for i, c in enumerate(s):
        if counter[c] == 1:
            return i
    return -1

print(first_non_repeating_char_index("leetcode"))
print(first_non_repeating_char_index("aabbss"))