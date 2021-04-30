https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:        
        temp = []
        for order in orders:            
            combi = combinations(sorted(order), c)            
            temp += combi            
        counter = Counter(temp)        
        
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]                         
    return sorted(answer)


import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

        print(result)

    return [ ''.join(v) for v in sorted(result) ]