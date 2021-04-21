def solution(s):
    stack = []
    for word in s:
        if stack:
            if stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
        else:
            stack.append(word)
    return 0 if stack else 1

s= 'baabaa'

for word in s:
    word = 'b'
    else:
        stack.append(word) stack = ['b']
    word = 'a'
    else:
        stack.append(word) stack = ['b','a']
    word = 'a'
    if stack:
        if stack[-1:a] == word:a:
            stack.pop() stack = ['b']
    word = 'b'
        if stack[-1:b] == word:b:
            stack.pop() stack = []
    word = 'a'
    else:
        stack.append(word) stack = ['a']
    word = 'a'
        if stack[-1:a] == word:a:
            stack.pop() stack = []