"""
Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:
1 <= n <= 45
"""

def main(n):
    if n <= 2:
        print(n)
        return
    else:
        # step(n) = fib(n+1) = fib(n-1) + fib(n+1)
        n = n+1

    cost = [0] * (n+1)

    cost[0] = 0
    cost[1] = 1

    for i in range(2, n+1):
        cost[i] = cost[i - 1] + cost[i - 2]

    print(cost)
    print(cost[-1])


if __name__ == "__main__":
    main(1)
    main(2)
    main(3)