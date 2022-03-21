# https://www.acmicpc.net/problem/1495
# 기타리스트
# dp


# [
#   [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
#   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#   [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 
#   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# ]
# 시작점에서 부터 0에서 최대볼륨 사이의 값일 경우에만 1을 기록해 나감. 마지막에 역순으로 루프를 돌며 값 찾음.

N, S, M = map(int, input().split()) # 곡의 개수, 시작 볼륨, 최대 볼륨
arr = list(map(int, input().split())) # 볼륨 조정 개수

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
dp[0][S] = 1
arr = [0] + arr

for i in range(1, N+1):
  for j in range(M+1):
    if dp[i-1][j] == 1:
      if j - arr[i] >= 0:
        dp[i][j - arr[i]] = 1
      if j + arr[i] <= M:
        dp[i][j + arr[i]] = 1
    
result = -1
for i in range(M, -1, -1):
  if dp[N][i] == 1:
    result = i
    break

print(result)