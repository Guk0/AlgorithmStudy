# https://www.acmicpc.net/problem/9465
# 스티커
# DP

from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())

  dp1 = list(map(int, input().split()))
  dp2 = list(map(int, input().split()))
  for i in range(1, N):
    if i > 1:
      dp1[i] = max(dp2[i-1], dp2[i-2], dp1[i-2]) + dp1[i]
      dp2[i] = max(dp1[i-1], dp2[i-2], dp1[i-2]) + dp2[i]
    else:
      dp1[i] = dp2[i-1] + dp1[i]
      dp2[i] = dp1[i-1] + dp2[i]

  print(max(dp1[N-1], dp2[N-1]))

  # 10 50 60 130 210 210 40
  # 20 50 80 110 190 230 80

  # 20 30 50 100 80

  # 270
  # 290