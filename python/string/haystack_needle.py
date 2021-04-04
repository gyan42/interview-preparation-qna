"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


print(Solution().strStr("helloworld", "wor"))
print(Solution().strStr("helloworld", "words"))

print("===============================================================================================================")

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        res = -1
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    break # move to next char in haystack and continue
            else:
                return i
        else:
            return -1

print(Solution().strStr("helloworld", "wor"))
print(Solution().strStr("helloworld", "words"))
