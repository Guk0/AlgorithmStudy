# https://programmers.co.kr/learn/courses/30/lessons/64065
# 튜플

def solution(s):
    answer = []
    strings = []
    string = s[2:-2].split("},{")
    
    for el in string:
        strings.append(list(map(int, el.split(","))))
    
    strings.sort(key=lambda x:len(x))
    
    for el in strings:
        for el2 in el:
            if not el2 in answer:
                answer.append(el2)
    
    return answer