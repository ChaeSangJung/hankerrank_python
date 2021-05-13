https://www.hackerrank.com/challenges/mark-and-toys/problem

def maximumToys(prices, k):
    # Write your code here
    sort_prices = sorted(prices) 
    count = 0 
    for i in range(len(sort_prices)): 
        k = k - sort_prices[i] 
        if k < 0 : 
            break 
        count = count + 1 
    return count