https://www.hackerrank.com/challenges/two-arrays/problem

def twoArrays(k, A, B):
    count=0 # 기준이 될 리스트 A의 index
    i=0 # B의 index
    
    A.sort(reverse=True) # A를 내림차순으로 정렬
    B.sort() # B를 오름차순으로 정렬(가능한 작은 수로 A[count]+B[i]>=k가 충족되도록 함)
    while count<=(n-1): 
        if A[count]+B[i] >= k: # 두 값의 합이 k와 같거나 클 경우 
            B[count],B[i]=B[i],B[count] # B의 값 위치를 바꾼다
            count+=1 # 해당 값을 고정시키고 다음 index로 넘어감
            i=count

        else: # 두 값의 합이 k보다 작을 경우
            if i==(n-1):
                return 'NO'
            else: 
                i+=1 # 다음 index로 넘어감
    return 'YES'

n = 3
k = 10
A = [2, 1, 3]
B = [7, 8, 9]

solution 
A = [3, 2, 1] 
B = [7, 8, 9]