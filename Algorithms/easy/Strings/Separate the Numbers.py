https://www.hackerrank.com/challenges/separate-the-numbers/problem

def validate(s, first):
    while s:
        if s.startswith(first):
            s = s[len(first):]
            first = str(int(first) + 1)
        else:
            return False
    return True

def separateNumbers(s):
    if s[0] == '0' and len(s) > 1: # condition 2
        return "NO"
    else:
        for ind in range(1, len(s)//2 + 1):
            first = s[:ind]
            if validate(str(s), first):
                return "YES " + first
    return "NO"

s = '99100101'

for ind in range(1, 'len(s)//2 + 1'3):
    ind = 1
    first = s[:ind] first= '9'
    if validate(str(s), first '9'):
        while s: s = '99100101'
            if s.startswith(first '9'): true
                s = s[len(first), 1:] s= '9100101'
                first = str(int('9') + 1), '10'
        while s: s = '9100101'
            if s.startswith(first '10'): false
            else : return False

    ind = 2
    first = s[:ind,2] first= '99'
    
    if validate(str(s), first '99'):
        while s: s = '99100101'
            if s.startswith(first '99'): true
                s = s[len(first), 2:] s= '100101'
                first = str(int('99') + 1), '100'
        while s: s = '100101'
            if s.startswith(first '100'): true
                s = s[len(first), 3:] s= '101'
                first = str(int('100') + 1), '101'
        while s: s = '101'
            if s.startswith(first '101'): true
                s = s[len(first), 3:] s= ''
                first = str(int('100') + 1), '102'
        return true
    
            return "YES " + first '99'
