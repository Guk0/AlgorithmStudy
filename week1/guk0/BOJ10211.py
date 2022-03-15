# https://www.acmicpc.net/problem/10211
# Maximum Subarray
# DP

from sys import stdin

T = int(stdin.readline())

for _ in range(T):
  N = int(stdin.readline())
  arr = list(map(int, stdin.readline().split()))

  dp = [0]*N
  dp[0] = arr[0]

  for i in range(1, N):
    dp[i] = max(dp[i-1]+arr[i], arr[i])
    print(dp)
    
  print(max(dp))

# -2 -2 1 3 -5
