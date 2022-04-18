"""
How many ways to traverse a [m x n] grid with restrictions of going only right or down?

"""

def grid_travel(m,n, memo={}):
    """

    :param m: Total number of rows
    :param n: Total number of columns
    :return:
    """
    if f"m{m}n{n}" in memo:
        return memo[f"m{m}n{n}"]

    if (m == 1 and n==1):
        memo[f"m{m}n{n}"] = 1
        return memo[f"m{m}n{n}"]
    elif (m ==0 or n ==0):
        memo[f"m{m}n{n}"] = 0
        return memo[f"m{m}n{n}"]
    else:
        memo[f"m{m}n{n}"] = grid_travel(m-1, n, memo) + grid_travel(m, n-1, memo)
        return memo[f"m{m}n{n}"]


if __name__ == "__main__":
    print("1 x 1 : ", grid_travel(1, 1))
    print("2 x 3 : ", grid_travel(2, 3))
    print("3 x 2 : ", grid_travel(3, 2))
    print("3 x 3 : ", grid_travel(3, 3))
    print("5 x 5 : ", grid_travel(5, 5))
    print("20 x 20 : ", grid_travel(18, 18))
    print("200 x 200 : ", grid_travel(200, 200))
