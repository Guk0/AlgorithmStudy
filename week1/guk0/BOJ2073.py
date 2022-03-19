# https://www.acmicpc.net/problem/2073
# 수도배관공사

from sys import stdin

D, P = map(int, stdin.readline().split()) # 수도관을 설치하려는 거리, 파이프 개수
# 수도관의 용량은 파이프의 용량 중 최솟값.
# 수도관의 용량의 최댓값을 구하라.

arr = [list(map(int, stdin.readline().split())) for _ in range(P)]

dp = [0 for _ in range(D+1)]
dp[0] = 1e9

for length, capacity in arr:
  for j in range(D, length-1, -1):
  # for j in range(length, D+1):
    dp[j] = max(dp[j], min(dp[j-length], capacity))
    print(dp)

print(dp[D])
