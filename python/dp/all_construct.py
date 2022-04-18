"""
Given a target and array  of strings, the function should return a 2D array
containing all of the ways that the target can be constructed by concatenating the 
elements int he wordbank array. 

Each element in the return array should represent one combination that constructs the target
"""

"""
base cases:
all_construct("hello", ["can", "wo", "h]) => [] # Negative
all_construct("", ["can", "wo", "h]) => [[]] # Positive


O(n^m*m)
O(m) # size of massize array are not considered for calculation
"""

#                   m        n
def all_construct(target, word_bank, memo={}):

    if target in memo:
        return memo[target]

    if target in memo:
        return memo[target]

    if target == '':
        return [[]]

    res = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = list(map(lambda l: l + [word], suffix_ways))
            res.extend(target_ways)

    memo[target] = res

    return res


print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
# print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"], dict()))  # 5
"""
[
[ab, cd, ef]
[ab, c, def]
[abc, def]
[abcd, ef]
]
"""

print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # 0
print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # 4
print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # 0
