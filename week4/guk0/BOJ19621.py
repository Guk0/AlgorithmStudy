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
# compression_arr = [0]
# compression_index_dict = {}

# for i in range(len(arr)):
#   compression_arr = compression_arr + [arr[i][0], arr[i][1]]

# compression_arr.sort()
# arr.sort(key=lambda x : x[1])

# for i in range(len(set(compression_arr))):
#   if compression_arr[i] not in compression_index_dict:
#     compression_index_dict[compression_arr[i]] = i

# dp = [0] * len(compression_arr)

# arr_index = 0
# for i in range(1, len(compression_index_dict.keys())):
#   end = arr[arr_index][1]
#   if i == compression_index_dict[end]:
#     current = dp[compression_index_dict[arr[arr_index][0]]] + arr[arr_index][2]
#     dp[i] = max(current, dp[i-1])
#     arr_index += 1
#   else:
#     dp[i] = dp[i-1]

# print(dp[-1])