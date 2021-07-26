# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import Counter, defaultdict


def isValid(s):
    # Write your code here
    if s is None:
        return "YES"
    if len(s) == 1 or len(s) == 0:
        return "YES"
    c = Counter(s)
    g = defaultdict(lambda: 0)
    for k, v in c.items():
        g[v] += 1
    if len(g) == 1:
        return "YES"
    if len(g) > 2:
        return "NO"
    if list(g.values())[1] != 1:
        return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
