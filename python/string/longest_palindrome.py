"""
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length,
return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic
 substring of "bananas" is "anana".
"""

from itertools import combinations

def is_palindrome(string):
    return string == string[::-1]

def find_longest_palindrome(string):
    longest_sub_string = ""
    for i in range(len(string)+1):
        for sub_Str in combinations(string, i):
            if is_palindrome(sub_Str) and len(sub_Str) > 2:
                if len(longest_sub_string) < len(sub_Str):
                    longest_sub_string = sub_Str
    print("".join(longest_sub_string))
    return longest_sub_string

find_longest_palindrome("aabcdcb")
find_longest_palindrome("bananas")
