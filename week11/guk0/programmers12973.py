# https://programmers.co.kr/learn/courses/30/lessons/12973
# 짝지어 제거하기
# 스택


def solution(s):
    arr = []
    for i in range(len(s)):
        if arr and arr[-1] == s[i]:
            arr.pop()
            continue

        arr.append(s[i])
        
        
    
    return 0 if arr else 1

# slicing으로 하면 시간초과남

# def solution(s):
#     answer = -1
#     i = 1
#     while s and i < len(s):
#         if i >= 1 and s[i] == s[i-1]:
#             s = s[:i-1] + s[i+1:]
#             i -= 1
#         else:
#             i += 1            
    
#     return 1 if len(s) == 0 else 0



