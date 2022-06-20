# https://programmers.co.kr/learn/courses/30/lessons/77486
# 다단계 칫솔 판매

# seller들 loop 돌면서 seller의 최상위 루트까지 계속 profit을 추가하는 방식
# 시간이 초과한 것은 while안에 profit == 0 조건이 없어서 그런거였음. 그거아니면 그냥 통과함.
# 그리고 * 0.1 보다는 // 10이 맞다.

import math

def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = [0 for _ in range(n)]    
    indexes = {}
    for i in range(n):
        indexes[enroll[i]] = i
    
    for i in range(len(seller)):
        current_index = indexes[seller[i]]
        
        profit = amount[i] * 100        
        
        while True:
            if profit == 0:
                break
                
            if profit // 10 > 0:
                parent_profit = profit // 10
                child_profit = profit - parent_profit
            else:
                parent_profit = 0
                child_profit = profit
                            
            answer[current_index] += child_profit            
            
            if referral[current_index] == "-":
                break
                
            profit = parent_profit
            current_index = indexes[referral[current_index]]
    
    return answer