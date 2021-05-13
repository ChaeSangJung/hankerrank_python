https://www.hackerrank.com/challenges/pangrams/problem

def pangrams(s):
    # Write your code here
    ascii_array = []
    lower_string = s.lower().replace(" ","")
    for i in range(len(lower_string)):
        ascii_array.append(ord(lower_string[i]))

    print(lower_string)
    print(ascii_array)
    for i in range(97, 123):
        if i not in ascii_array:
            return 'not pangram'
    return 'pangram'


alphabet = 'abcdefghijklmnopqrstuvwxyz'
def pg(x):
    for letter in alphabet:
        if letter not in x:
            return False
        
    return True
sentence = input()
sentence = sentence.lower()
if pg(sentence):
    print("pangram")
else:
    print("not pangram")