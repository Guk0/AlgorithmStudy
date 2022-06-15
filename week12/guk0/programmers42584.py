# https://programmers.co.kr/learn/courses/30/lessons/42584
# 주식가격

def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i-j
            
        stack.append(i)
        
    for index in stack:
        answer[index] = len(prices) - index -1
    
    return answer