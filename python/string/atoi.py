"""
Input: s = "42"
Output: 42

Input: s = "   -42"
Output: -42

Input: s = "4193 with words"
Output: 4193

Input: s = "words and 987"
Output: 0

Input: s = "-91283472332"
Output: -2147483648

Input "00000-42a1234"
Output: -42

"""


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s.strip() == "":
            return 0

        res = 0
        i = 0
        sign = None

        s = s.lstrip()
        if s[0] == "-":
            sign = -1
            i = 1
        if s[0] == "+":
            sign = 1
            i = 1

        for c in s[i:]:
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                res = (res * 10) + int(c)
            else:
                break

        if sign is None:
            sign = 1

        res = res * sign

        if res < -2 ** 31:
            res = -2 ** 31
        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1

        return res
print(Solution().myAtoi(s="   -42"))
print(Solution().myAtoi(s="42"))
print(Solution().myAtoi(s=""))
print(Solution().myAtoi(s=" "))