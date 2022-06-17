# https://programmers.co.kr/learn/courses/30/lessons/42883
# 큰 수 만들기

def solution(number, k):
    answer = ''
    stack = []
    
    for el in number:
        while stack and k > 0 and int(el) > int(stack[-1]):
            k -= 1
            stack.pop()
        
        stack.append(el)
        
    while stack and k > 0:
        k -= 1
        stack.pop()
        
    
    return "".join(stack)