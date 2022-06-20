# https://programmers.co.kr/learn/courses/30/lessons/42578
# 위장

def solution(clothes):
    answer = 1
    clothes_dict = {}
    
    for el in clothes:
        if el[1] in clothes_dict:
            clothes_dict[el[1]].append(el[0])
        else:
            clothes_dict[el[1]] = [el[0]]
        
    
    for length in map(len, clothes_dict.values()):
        answer *= (length+1)
        
    return answer-1