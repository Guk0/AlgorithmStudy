# https://www.acmicpc.net/problem/14728
# 벼락치기


from sys import stdin


N, T = map(int, stdin.readline().split()) # 단원의 개수, 제한 시간

arr = [list(map(int, stdin.readline().split())) for _ in range(N)] # 단원의 예상 공부시간, 배점
arr = [[0, 0]] + arr

dp = [[0 for _ in range(T+1)] for _ in range(N+1)]

for i in range(1, N+1):
  for j in range(1, T+1):
    if arr[i][0] <= j:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i][0]] + arr[i][1])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[N][T])
