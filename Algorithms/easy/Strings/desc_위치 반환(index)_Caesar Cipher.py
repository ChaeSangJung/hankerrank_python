https://www.hackerrank.com/challenges/caesar-cipher-1/problem

import string
# Complete the caesarCipher function below.
symbols_low = string.ascii_lowercase
symbols_up = string.ascii_uppercase

def caesarCipher(s, k):
  res = []
  for c in s:        
    if c.isupper():
        res.append(symbols_up[(symbols_up.index(c)+k)%len(symbols_up)])
    elif c.islower():
        res.append(symbols_low[(symbols_low.index(c)+k)%len(symbols_low)])
    else:
        res.append(c)
                      
  return "".join(map(str, res))

s = 'middle-Outz'
k = 2


               0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
symbols_low = 'a b c d e f g h i j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z'

              0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
symbols_up = 'A B C D E F G H I J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z'

s = 'middle-Outz'
k = 2

               0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
symbols_low = 'a b c d e f g h i j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z'

              0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
symbols_up = 'A B C D E F G H I J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z'

s = 'middle-Outz'
k = 2

for c in s:
    c = 'm'
    res.append(symbols_low[(symbols_low.index(c:'m' 12)+k:2 => 14)%len(symbols_low):26])
               symbols_low[14] => 'o'
    
    c='i'
    res.append(symbols_low[(symbols_low.index(c:'i' 8)+k:2 => 10)%len(symbols_low):26])
               symbols_low[10] => 'k'
    
    c='d'
    res.append(symbols_low[(symbols_low.index(c:'d' 3)+k:2 => 5)%len(symbols_low):26])
               symbols_low[5] => 'f'

    c='d'
    res.append(symbols_low[(symbols_low.index(c:'d' 3)+k:2 => 5)%len(symbols_low):26])
               symbols_low[5] => 'f'

    c='l'
    res.append(symbols_low[(symbols_low.index(c:'l' 11)+k:2 => 13)%len(symbols_low):26])
               symbols_low[13] => 'n'

    c='e'
    res.append(symbols_low[(symbols_low.index(c:'e' 4)+k:2 => 6)%len(symbols_low):26])
               symbols_low[6] => 'g'

    c='-'
    res.append(c:'-')

    c='O'
    res.append(symbols_low[(symbols_low.index(c:'O' 14)+k:2 => 16)%len(symbols_low):26])
               symbols_low[16] => 'Q'

    c='u'
    res.append(symbols_low[(symbols_low.index(c:'u' 20)+k:2 => 22)%len(symbols_low):26])
               symbols_low[22] => 'w'

    c='t'
    res.append(symbols_low[(symbols_low.index(c:'t' 19)+k:2 => 21)%len(symbols_low):26])
               symbols_low[21] => 'v'

    c='z'
    res.append(symbols_low[(symbols_low.index(c:'z' 25)+k:2 => 27)%len(symbols_low):26])
               symbols_low[1] => 'b'


위치 반환(index)
index(x) 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.

>>> a = [1,2,3]
>>> a.index(3)
2
>>> a.index(1)
0
위 예에서 리스트 a에 있는 숫자 3의 위치는 a[2]이므로 2를 돌려주고, 숫자 1의 위치는 a[0]이므로 0을 돌려준다.

다음 예에서 값 0은 a 리스트에 존재하지 않기 때문에 값 오류(ValueError)가 발생한다.

>>> a.index(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 0 is not in list