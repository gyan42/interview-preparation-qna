# https://leetcode.com/problems/making-file-names-unique/
# https://leetcode.com/problems/making-file-names-unique/discuss/996360/Python-Caching-(k)

class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        print(names)
        ret = []
        cache = {}

        for name in names:
            new_name = name
            if new_name not in cache:
                ret.append(new_name)
            else:
                i = cache[new_name]
                while f"{name}({i})" in cache:
                    i += 1
                new_name = f"{name}({i})"
                cache[new_name] = i
                ret.append(new_name)

            cache[new_name] = 1

        return ret

# res = Solution().getFolderNames(names = ["pes","fifa","gta","pes(2019)"])
# print(res)
#
# res = Solution().getFolderNames(names = ["gta","gta(1)","gta","avalon"])
# print(res)
#
# res = Solution().getFolderNames(names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"])
# print(res)
#
# res = Solution().getFolderNames(names = ["wano","wano","wano","wano"])
# print(res)
#
# res = Solution().getFolderNames(names=["kaido", "kaido(1)", "kaido", "kaido(1)"])
# print(res)

res = Solution().getFolderNames(names=["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"])
print(res)

