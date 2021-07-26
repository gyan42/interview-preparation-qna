"""
https://www.geeksforgeeks.org/check-given-string-valid-number-integer-floating-point/
https://leetcode.com/problems/valid-number/
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        # 0-9 + - . eE
        # ord
        # case1: Intergers
        # Case 1a: Handling the sign
        # Case 2: Floating
        # Case 2a: Validating Sign
        # Case 2b: Val dec.point
        # Case 2c: Validate e/E
        e = False
        sign = False
        for i in range(len(s)):
            c = s[i]
            if not (c >= '0' and c <= '9') and c not in ['.', '+', '-', 'e', 'E']:
                return False
            if c in ['+', '-'] and sign and not e:  # +6e-1
                return False
            if c in ['+', '-']:
                sign = True
                continue

            if e and c == '.':
                return False

            if c in ['e', 'E']:
                if e:
                    return False
                e = True
                # if s is begining, since 0-1= -1 will give end of the string
                if s[0] == 'e':
                    return False
                if not (s[i - 1] >= '0' and s[i - 1] <= '9'):
                    return False
                if i + 1 >= len(s):
                    return False
                continue

        return True


print("*" * 100)
for s in ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]:
    print(s, Solution().isNumber(s))

print("*" * 100)
for s in ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]:
    print(s, Solution().isNumber(s))
print("*" * 100)