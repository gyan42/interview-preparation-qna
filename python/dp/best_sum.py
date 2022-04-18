"""
Given list of values and a target sum, find the best pair that makes the sum with least number of combination

"""


def best_sum(target_sum, values, memo):

    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    best_pair = None

    for value in values:
        ret = best_sum(target_sum=target_sum - value, values=values, memo=memo)
        if ret is not None:
            res = ret + [value]
            if best_pair is None or len(res) < len(best_pair):
                best_pair = res
                memo[target_sum] = best_pair
                # return best_pair # Dont return the value until all possible combinations are evaluated for child tree

    memo[target_sum] = best_pair
    return memo[target_sum]


print(best_sum(7, [2, 3], {}))
print(best_sum(7, [5, 3, 4, 7], {}))
print(best_sum(7, [2, 4], {}))
print(best_sum(8, [2, 5, 3], {}))
print(best_sum(8, [2, 3, 5], {}))
print(best_sum(300, [7, 14], {}))
print(best_sum(4830, [7, 14], {}))


""""
                                             8
                                        /    |    \                                
                                    #-2      #-3    #-5
                                   /         |         \
                                /            |             \
                            /                |                 \
                        /                    |                      \
                    6                        5                       3
                /   |   \                 /   |   \                /  |  \
             #-2  #-3  #-5              #-2 #-3  #-5             #-2 #-3 #-5
            /       |    |               |    |   |               |   |  |
            4       3    1               3    2   0               1   0  -2
           / \     /  \                 / \   | 
        #-2  #-3  #-2 #-3             #-2 #-3 #-2
          |   |   |    |               |  |   | 
          2   1   1    0               1  0   0
          |
        #-2
          0              
 



"""