https://programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    m = m.replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g').replace('A#','a')
    music_dic = dict()
    answer = ["",""]
    for information in musicinfos:
        start, end, name, music = information.split(',')
        music = music.replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g').replace('A#','a')
        start =[int(time) for time in start.split(':')]
        end = [int(time) for time in end.split(':')]
        all_time = (end[0]-start[0])*60 + (end[1]-start[1])
        music = music*(all_time//len(music)) + music[0:all_time%len(music)]
        music_dic[name] = music
    for key,value in music_dic.items():
        if m in value:
            if len(answer[1]) < len(value): 
                answer[0] = key
                answer[1] = value
    return "(None)" if len(answer[0]) == 0 else answer[0]

m	= "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

딕셔너리 쌍 추가하기
>>> a = {1: 'a'}
>>> a[2] = 'b'
>>> a
{1: 'a', 2: 'b'}
{1: 'a'} 딕셔너리에 a[2] = 'b'와 같이 입력하면 딕셔너리 a에 Key와 Value가 각각 2와 'b'인 2 : 'b'라는 딕셔너리 쌍이 추가된다.

>>> a['name'] = 'pey'
>>> a
{1: 'a', 2: 'b', 'name': 'pey'}
딕셔너리 a에 'name': 'pey'라는 쌍이 추가되었다.

>>> a[3] = [1,2,3]
>>> a
{1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
Key는 3, Value는 [1, 2, 3]을 가지는 한 쌍이 또 추가되었다.

딕셔너리 요소 삭제하기
>>> del a[1]
>>> a
{2: 'b', 'name': 'pey', 3: [1, 2, 3]}
위 예제는 딕셔너리 요소를 지우는 방법을 보여 준다. del 함수를 사용해서 del a[key]처럼 입력하면 지정한 Key에 해당하는 {key : value} 쌍이 삭제된다.