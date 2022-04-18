"""
Minimal moves to form a string

Given a string S, check if it is possible to construct the given string S by performing any of the below operations any number of times. In each step, we can:

Add any character at the end of the string.
or, append the string to the string itself.
The above steps can be applied any number of times. The task is to find the minimum steps required to form the string.

Example 1:

Input: S = "aaaaaaaa"
Output: 4
Explanation:
move 1: add 'a' to form "a"
move 2: add 'a' to form "aa"
move 3: append "aa" to form "aaaa"
move 4: append "aaaa" to form "aaaaaaaa"


â€‹Example 2:

Input: S = "abcabca"
Output: 5
Explanation:
move 1: add 'a' to form "a"
move 2: add 'b' to form "ab"
move 3: add 'c' to form "abc"
move 4: append "abc" to form "abcabc"
move 5: add 'a' to form "abcabca"
"""

import sys


def main(data):
    # print(data)

    # cost = [i for i in range(0, len(data))]
    cost = [10000000] * len(data)
    s1 = data[0]
    cost[0] = 1
    s2 =""

    for i in range(1, len(data)):
        s1 = s1 + data[i]
        cost[i] = min(cost[i], cost[i-1]+1)
        s2 = data[i+1:2*i+2]

        if s1 == s2:
            cost[1+2*i] = min(cost[i]+1, cost[1+2*i])
            print(i, ":", cost)
        else:
            print(i, ":", cost)
    return cost[-1]


if __name__ == '__main__':
    if len(sys.argv)>1:
        main(sys.argv[1])
    else:
        print("\nRes: ", main("aaaaaaaa"))
        print("\nRes: ", main("abcabcd"))
        print("\nRes: ", main("abcdefgh"))
