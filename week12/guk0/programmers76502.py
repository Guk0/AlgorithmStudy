# https://programmers.co.kr/learn/courses/30/lessons/76502
# 괄호 회전하기

def solution(s):
    answer = 0
    dictionary = {"]": "[", "}": "{", ")": "("}
    target = dictionary.keys()
    
    for i in range(len(s)):
        tmp_s = s[i:] + s[:i]
        stack = []

        for char in tmp_s:        
            if stack and char in target and stack[-1] == dictionary[char]:
                stack.pop()
            else:
                stack.append(char)
        
        if len(stack) == 0:
            answer += 1
    
    return answer
