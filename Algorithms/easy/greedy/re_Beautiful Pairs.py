https://www.hackerrank.com/challenges/beautiful-pairs/problem

def beautiful_pairs(A, B):
    A = sorted(A)
    B = sorted(B)
    count = i = j = 0
    while i < n and j < n:
        if A[i] == B[j]:
            count += 1
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    if count == n:
        return count-1
    return count+1
