https://www.hackerrank.com/challenges/strange-advertising/problem

def viralAdvertising(n):
    shared_num = 5
    cumulative_num = 0
    
    for i in range(n):
        like_num = shared_num//2
        cumulative_num += like_num
        shared_num = like_num*3
    return cumulative_num