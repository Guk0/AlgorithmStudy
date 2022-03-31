# https://www.acmicpc.net/problem/1932
# 정수 삼각형
# DP


from sys import stdin

input = stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
k = 2
for i in range(1, N):
  for j in range(k):
    if j == 0:
      arr[i][j] += arr[i-1][0]
    elif j == i:
      arr[i][j] += arr[i-1][j-1]
    else:  
      arr[i][j] += max(arr[i-1][j], arr[i-1][j-1])
  k += 1


print(max(arr[N-1]))

#         7
#       3   8
#     8   1   0
#   2   7   4   4
# 4   5   2   6   5
