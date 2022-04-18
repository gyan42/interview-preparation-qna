"""

Write a function that accepts a target string and a wordbank array of strings.

The function should return the number of ways that the target can be constructed
by concatenating elements of the wordbank array.

You may reuse elements of wordbank as many times as needed.
"""


"""

O_time(n^m * m)                      O(n*m*m)

O_space(m*m) # m stack level        O(m*m)
             # m operation to slice the string


"""

#                    m        n
def can_construct(target, word_bank, memo={}):

    if target in memo:
        return memo[target]

    if target == '':
        return True # When we found a way reconstruct the string

    # Return true if any of branch returns true
    for word in word_bank:
        # check for matching prefix
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, word_bank):
                memo[suffix] = True
                return True

    # If no branch leads to positive case, return false
    memo[target] = False
    return False



print(can_construct("purple", ["purp", "p", "ur", "le", "purpl"])) # true
print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # true
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # false
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # true
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeh", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # false
