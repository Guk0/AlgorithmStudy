# https://programmers.co.kr/learn/courses/30/lessons/12909
# 올바른 괄호


def solution(s):
    answer = True
    stack = []
    
    for el in s:
        if stack and stack[-1] == "(" and el == ")":
            stack.pop()
        else:
            stack.append(el)
    
    if stack:
        answer = False

    return answer