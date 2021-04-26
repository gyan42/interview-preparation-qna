"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).


"""
def checkPossibility(nums):
    """
    :param nums:
    :return:
    """
    modified = False
    size = len(nums)
    for i in range(len(nums)-1):
        if nums[i] > nums[i + 1]:
            if modified:
                return False
            """
                            i-1 i   i+1
                1   2   3   4   6   5    --->  1  2  3  4  5  6
                            i   i+1 i+2   
                3   4   5   3   6   8    --->  3  3  4  5  6  8
                    i-1 i   i+1 i+2
                3   4   5   3   3   8    --->  3  4  5  3  3  8
            """
            if i - 1 < 0 or nums[i - 1] <= nums[i + 1]:
                # in this case, you can change nums[i] = x   (nums[i - 1] <= x <= nums[i + 1])
                pass
            elif i + 2 >= size or nums[i] <= nums[i + 2]:
                # in this case, you can change nums[i + 1] = x  (nums[i] <= x <= nums[i + 2])
                pass
            else:
                # if it's not the both of them, it's not possible to make sorted state with one modification
                return False
            modified = True
    return True

print(checkPossibility([1,2,3,4,5,6]))
print(checkPossibility([1,2,4,3,5,6]))
print(checkPossibility([3,4,5,3,6,8]))
print(checkPossibility([3,4,5,3,3,8]))

