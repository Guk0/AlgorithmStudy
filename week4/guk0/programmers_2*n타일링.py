# https://programmers.co.kr/learn/courses/30/lessons/12900
# 2*n 타일링
# DP
#  % 1000000007 를 마지막에 return할때만 하면 시간초과됨. loop안에서 dp구할때 %를 계속 해줘야함.

def solution(n):  
    dp = [0] * n
    dp[0], dp[1] = 1, 2
    
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    
    return dp[n-1]