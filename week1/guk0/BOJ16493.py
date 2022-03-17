# https://www.acmicpc.net/problem/16493
# 최대 페이지 수

# 최대 페이지수
# 첫째 줄에 N(1 ≤ N ≤ 200)과 챕터의 수 M(1 ≤ M ≤ 20)이 주어진다. 
# 둘째 줄부터 각 챕터 당 읽는데 소요되는 일 수와 페이지 수가 주어진다


from sys import stdin

N, M = map(int, stdin.readline().split()) # 날짜, 챕터수

arr = [list(map(int, stdin.readline().split())) for _ in range(M)]
arr = [0] + arr

dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

for i in range(1, M+1):
  for j in range(1, N+1):
    if arr[i][0] <= j:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i][0]] + arr[i][1])
    else:
      dp[i][j] = dp[i-1][j]


print(dp[M][N])

# 7 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200
#     (3 10) (5 20) (1 10) (1 10) (2 15) (4 40) (2 200)
# 1     0      0      10
# 2     0      0      10
# 3     10     10     10
# 4            10     20
# 5            20
# 6
# 7
