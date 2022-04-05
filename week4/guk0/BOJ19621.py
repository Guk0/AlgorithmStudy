# https://www.acmicpc.net/problem/19621
# 회의실 배정2, 3, 4

# 회의실 배정 2, 3
from sys import stdin

input = stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * N
dp[0] = arr[0][2]

for i in range(1, len(arr)):
  if i > 1:
    dp[i] = max(dp[i-1], dp[i-2] + arr[i][2])
  else:
    dp[i] = max(dp[i-1], arr[i][2])

print(dp[-1])


# 회의실 배정 4
# from sys import stdin

# input = stdin.readline

# N = int(input())

# arr = [list(map(int, input().split())) for _ in range(N)]
# compression_arr = []

# for el in arr:
#   compression_arr = compression_arr + [el[0], el[1]]

# compression_arr.sort()
# # arr.sort()


# dp = [0] * len(compression_arr)

# for i in range(len(compression_arr)):
#   if 

# print(dp[-1])