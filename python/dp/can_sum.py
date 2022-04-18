"""

given a list of numbers and a target sum, return true if the combination of numbers in the list leads to the target sum.

Note: list numbers can be used any number of times

"""


"""
reduce the target sum till it reaches 0, if so return true or otherwise

Time: O(n^m)
Space: O(n+m)

With Memo:

"""


def can_sum(target_sum, values, memo={}):
    """

    :param target_sum:
    :param values: list
    :return:
    """
    # print(memo, values)
    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for value in values:
        reminder = target_sum - value
        if can_sum(reminder, values, memo):
            memo[target_sum] = True
            return True

    # If no way leads to zero then there is no possible values leads to sum
    memo[target_sum] = False
    return False


print(can_sum(7, [2, 3], {}))
print(can_sum(7, [5, 3, 4, 7], {}))
print(can_sum(7, [2, 4], {}))
print(can_sum(8, [2, 3, 5], {}))
print(can_sum(300, [7, 14], {}))


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