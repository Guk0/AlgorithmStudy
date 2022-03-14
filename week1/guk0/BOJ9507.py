# https://www.acmicpc.net/problem/9507
# Generations of Tribbles
# DP

from sys import stdin

T = int(stdin.readline())

dp = [1, 1, 2, 4]

for i in range(4, 68):  
  dp.append(dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4])

for _ in range(T):
  N = int(stdin.readline())
  print(dp[N])

