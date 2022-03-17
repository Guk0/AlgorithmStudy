# https://www.acmicpc.net/problem/1535
# 안녕
# dp(배낭문제)

N = int(input())

death = [int(x) for x in input().split()]
happy = [int(x) for x in input().split()]

death, happy = [0] + death, [0] + happy

dp = [[0 for _ in range(101)] for _ in range(N+1)]

for i in range(1, N+1):
  for d in range(1, 101):
    if death[i] <= d:
      dp[i][d] = max(dp[i-1][d], dp[i-1][d-death[i]] + happy[i])
    else:
      dp[i][d] = dp[i-1][d]

print(dp[N][99])

# 1 2 3 4 6 5 15 100
# 1 2 3 4 5 4 40 49

#    (1, 1) (2, 2) (3, 3) (4, 4) (6, 5) (5, 4) (15 40), (100, 49)
# 1   1       1      1
# 2   1       2      2
# 3   1       3      3
# 4   1       3      4
# 5   1       3      5
# 6   1       3 
# 7   1
# 8   1
# 9   1
# ...
# 100