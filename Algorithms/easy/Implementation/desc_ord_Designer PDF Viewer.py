https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = zaba

def designerPdfViewer(h, word):
    n = len(word)
    cnt = 0
    result = 0

    for i in range(n):
        num = ord(word[i])-97
        if(cnt <= h[num]):
            cnt = h[num]

    result = n*cnt
    
    return result

ord
ord(c)는 문자의 유니코드 값을 돌려주는 함수이다.

※ ord 함수는 chr 함수와 반대이다.

>>> ord('a')
97
>>> ord('가')
44032