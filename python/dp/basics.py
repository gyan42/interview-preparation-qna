import time

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# s = time.time()
# print(fib(40)) # O(2^N)
# print("Time took: ", time.time() - s) #Time took:  30.00671100616455

def fib_top_down(n, cache):
    if cache[n] is not None:
        return cache[n]
    if n <= 1:
        return n
    else:
        # calculate for first time
        res = fib_top_down(n-1, cache) + fib_top_down(n-2, cache)
        cache[n] = res
        return res


s = time.time()
n = 400
print(fib_top_down(n, [None]*(n+1))) # Time took:  0.0002562999725341797
print("Time took: ", time.time() - s) # Time took:  0.0002562999725341797


def fib_bottom_up(n):
    if n <= 1:
        return n
    cache = [0] * (n+1)
    cache[0] = 0
    cache[1] = 1
    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]

s = time.time()
n = 400
print(fib_bottom_up(n))  # Time took:  0.0002562999725341797
print("Time took: ", time.time() - s)  # Time took:  0.0002562999725341797


# Check correctness here : http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable301.html


"""
https://towardsdatascience.com/beginners-guide-to-dynamic-programming-8eff07195667

You have to build a staircase in such a way that, each type of staircase should consist of 2 or more steps. 
No two steps are allowed to be at the same height — each step must be lower than the previous one. 
All steps must contain at least one brick. A step’s height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2, 
and the second step having a height of 1 i.e.(2,1). But when N = 5, there are two ways you can build a 
staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2).

N=3
#
##
21

N=4
#
#
##
31

N = 5
#
#
#
##
41

#
##
##
32
"""
def solution(n):
  a = [1]+[0]* n #All steps must contain at least one brick
  print(a)
  for i in range(1, n+1):
    for k in range(n, i-1, -1): #reversed(range(i, n+1)):
      a[k] = a[k-i] + a[k]
      print(k, k-1, a[k-1], a[k], a)
  print(a)
  return a[n] - 1

print("Number of ways to build stare case is:", solution(10))