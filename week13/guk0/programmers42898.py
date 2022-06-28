# https://programmers.co.kr/learn/courses/30/lessons/42898
# 등굣길

def solution(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            
            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1_000_000_007
        
        
#     for x, y in puddles:
#         dp[y-1][x-1] = -1
    
#     for i in range(n):
#         for j in range(m):
#             if dp[i][j] == -1:
#                 continue

#             if dp[i-1][j] == -1 and dp[i][j-1] == -1:
#                 dp[i][j] = 0
#             elif i > 0 and dp[i-1][j] == -1:
#                 if j > 0:
#                     dp[i][j] = dp[i][j-1]
#                 else:
#                     dp[i][j] = 0
#             elif j > 0 and dp[i][j-1] == -1:
#                 if i > 0:
#                     dp[i][j] = dp[i-1][j]
#                 else:
#                     dp[i][j] = 0                
#             elif i > 0 and j > 0:
#                 dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1_000_000_007
#             else:
#                 if i > 0:
#                     dp[i][j] = dp[i-1][j]
#                 elif j > 0:
#                     dp[i][j] = dp[i][j-1]
    
    return dp[n][m]