# https://www.acmicpc.net/problem/1446
# 지름길
# dp, 다익스트라


from sys import stdin

N, D = map(int, stdin.readline().split()) # 개수, 실제 총 길이

arr = [list(map(int, stdin.readline().split())) for _ in range(N)] # 실제 시작 길이, 실제 끝 길이, 지름길로 간 거리

dp = [i for i in range(D+1)]

for i in range(0, D+1):
  dp[i] = min(dp[i-1] + 1, dp[i])

  for start, end, length in arr:
    if start == i and end <= D:
      dp[end] = min(dp[end], dp[start] + length)

print(dp[D])
