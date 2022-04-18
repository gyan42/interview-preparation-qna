# https://www.geeksforgeeks.org/lru-cache-in-python-using-ordereddict/
# https://leetcode.com/problems/lru-cache/discuss/46121/lru-cache-implementation-in-python-w-explanation

from collections import OrderedDict

class LRUV1(object):
    def __init__(self, capacity):
        self._capacity = capacity
        self._cache = OrderedDict()

    def get(self, key):
        if key not in self._cache.keys():
            return False
        else:
            self._cache.move_to_end(key, last=True) # move the recently used data to tail
            return self._cache[key]

    def put(self, key, value):
        self._cache[key] = value
        self._cache.move_to_end(key, last=True) # move the recently used data to tail
        if len(self._cache) > self._capacity:
            self._cache.popitem(last=False) # Remove the head which is least used


if __name__ == "__main__":
    cache = LRUV1(2)
    cache.put(1, 1)
    print(cache._cache)
    cache.put(2, 2)
    print(cache._cache)
    cache.get(1)
    print(cache._cache)
    cache.put(3, 3)
    print(cache._cache)
    cache.get(2)
    print(cache._cache)
    cache.put(4, 4)
    print(cache._cache)
    cache.get(1)
    print(cache._cache)
    cache.get(3)
    print(cache._cache)
    cache.get(4)
    print(cache._cache)


