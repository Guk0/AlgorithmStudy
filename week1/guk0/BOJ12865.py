# https://www.acmicpc.net/problem/12865
# 평범한 배낭


from sys import stdin

N, K = map(int, stdin.readline().split()) # 물건의 개수, 배낭의 최대 무게

arr = [list(map(int, stdin.readline().split())) for _ in range(N)] # 물건의 무게(w), 가치(v)
  
arr = [[0, 0]] + arr

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
  for j in range(1, K+1):
    if arr[i][0] <= j:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i][0]] + arr[i][1])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[N][K])