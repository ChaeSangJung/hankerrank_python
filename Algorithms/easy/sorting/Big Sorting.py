https://www.hackerrank.com/challenges/big-sorting/problem

def bigSorting(unsorted):
    return sorted(unsorted, key = lambda x: (len(x), x))