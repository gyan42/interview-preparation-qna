import sys
from tqdm import tqdm

# Function to get minimum number of trials
# needed in worst case with n eggs and k floors
def eggDrop(num_eggs, num_floors):

    # If there are no floors, then no trials
    # needed. OR if there is one floor, one
    # trial needed.
    if (num_floors == 1 or num_floors == 0):
        return num_floors

    # We need num_floors trials for one egg
    # and num_floors
    if (num_eggs == 1):
        return num_floors

    min = sys.maxsize

    # Consider all droppings from 1st
    # floor to kth floor and return
    # the minimum of these values plus 1.
    for floor_num in range(1, num_floors + 1):

        res = max(eggDrop(num_eggs - 1, floor_num - 1),
                  eggDrop(num_eggs, num_floors - floor_num))
        if (res < min):
            min = res

    return min + 1

# Driver Code
if __name__ == "__main__":

    n = 3
    k = 20
    print("Minimum number of trials in worst case with",
          n, "eggs and", k, "floors is", eggDrop(n, k))

# This code is contributed by ita_c
