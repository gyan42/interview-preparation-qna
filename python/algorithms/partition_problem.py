
def partition_set(data):
    """
    Partition problem is to determine whether a given set can be partitioned into two subsets such that the 
    sum of elements in both subsets is the same. 
    :param data: 
    :return: 
    """
    if sum(data) % 2 == 0:
        max_val = max(data)
        data_copy = data[:]
        data_copy.remove(max_val)
        return [max_val], data_copy
    else:
        return False


if __name__ == "__main__":
    print(partition_set(data=[1, 5, 11, 5]))
    print(partition_set(data=[1, 5, 11, 4]))
    print(partition_set(data={2, 3, 4, 6}))