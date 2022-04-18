"""
like cansum but return possibile combinations what ever encountered first

O(n^m * m)     O(n * m * m)
O(m)             O(m * m)
"""


def how_sum(target_sum, values, memo={}):
    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for value in values:
        ret = how_sum(target_sum - value, values, memo)
        if ret is not None:
            ret.append(value)
            memo[target_sum] = ret
            return ret

    memo[target_sum] = None
    return None


print(how_sum(7, [2, 3], {}))
print(how_sum(7, [5, 3, 4, 7], {}))
print(how_sum(7, [2, 4], {}))
print(how_sum(8, [2, 3, 5], {}))
print(how_sum(300, [7, 14], {}))


"""
                                             8
                                        /    |    \                                
                                    #-2      #-3    #-5
                                   /         |         \
                                /            |             \
                            /                |                 \
                        /                    |                      \
                    6                        5                       3
                /   |   \                 /   |   \                /  |  \
             #-2  #-3  #-5              #-2 #-3  #-5              #-2 #-3 #-5
            /       |    |               |    |   |                |   |  |
            4       3    1               3    2   0                1   0  -2
           / \     /  \                  / \   | 
        #-2  #-3  #-2 #-3              #-2 #-3 #-2
          |   |   |   |                 |  |   | 
          2   1   1   0                 1  0   0
          |
        #-2
          0    
"""