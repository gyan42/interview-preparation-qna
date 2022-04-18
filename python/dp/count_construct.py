"""
Write a function that accepts a target string and an array of strings.

The function should return a the number of ways that the target can be constructed by the wordbank array

You may reuse the elements of wordbank array
"""



"""
O(n^m * m)   O(n*m*m)
O(m*m)        O(m*m)
"""

#                      m      n
def count_construct(target="", word_bank=[], memo={}):
    # print(target, word_bank, memo)
    if target in memo:
        return memo[target]

    if target == '':
        return 1

    count = 0
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            count += count_construct(suffix, word_bank)
            memo[suffix] = count

    memo[target] = count
    return count



if __name__ == "__main__":
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"], dict()))  # 5
    print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"], {}))  # 2
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))  # 1
    print()
    print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
    print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
    print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeh", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # 0
