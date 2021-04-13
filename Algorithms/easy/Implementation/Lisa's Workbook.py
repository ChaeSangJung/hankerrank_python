n = 5
k = 3
arr = [4, 2, 6, 1, 10]

count = 0
page = 1

for i in range(1, n+1):
  j = 1 # jth problem
  while (j <= arr[i-1]):
    if (j == page):
      count += 1
    if (j%k == 0): # page is over
      page +=1
    j += 1
  if (arr[i-1]%k !=0): 
    # next chapter, arr[2]에서 page 꽉 차게 있는 것은 제외 
    # "if (j%k == 0): # page is over"에서 이미 페이지 넘김
    # 다음 챕터의 page 준비
    page += 1
print(count)

range(1, 5+1): i=1
    j = 1
    while(j:1 <= arr[i:1 - 1]:4) : true
        if j:1 == page:1
            count:0 += 1 : count = 1
        j += 1 : j=2

    j = 2
    while(j:2 <= 4): true
        j += 1 : j=3
    
    j = 3
    while(j:3 <= 4): true
        if (j:3 % k:3 == 0)
            page:1 += 1 : page = 2
        j += 1 : j=4
    
    j=4
    if(arr[i:1 - 1]%k !=0)
        page:2 += 1 : page:3
