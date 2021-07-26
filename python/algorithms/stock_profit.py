"""
Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling
that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at
5 dollars and sell it at 10 dollars.
"""

def get_max_profit(lst):
    max_profit = 0
    curr_max_profit = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]: # if the prices goes up, add the diff to curr profit and update max_profit if needed
            curr_max_profit += lst[i] - lst[i-1]
            if curr_max_profit > max_profit:
                max_profit = curr_max_profit
        else:
            curr_max_profit = 0 # reset if price goes down

    return max_profit

print(get_max_profit([9, 11, 8, 5, 7, 10]))
print(get_max_profit([1, 7, 2, 3, 6, 7, 6, 7]))
