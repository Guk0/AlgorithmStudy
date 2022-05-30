# https://www.acmicpc.net/problem/2096
# 내려가기
# dp

# 아예 dp라는 배열(인풋을 받는)을 선언하지 않고 for문 안에서 인풋을 받는다.

from sys import stdin
input = stdin.readline

N = int(input())
min_arr = [0, 0, 0]
max_arr = [0, 0, 0]

min_tmp = [0, 0, 0]
max_tmp = [0, 0, 0]

for i in range(N):
  a, b, c = list(map(int, input().split()))

  min_tmp[0] = min(min_arr[0], min_arr[1]) + a
  min_tmp[1] = min(min_arr[0], min_arr[1], min_arr[2]) + b
  min_tmp[2] = min(min_arr[1], min_arr[2]) + c
  min_arr[0], min_arr[1], min_arr[2] = min_tmp[0], min_tmp[1], min_tmp[2]
  
  max_tmp[0] = max(max_arr[0], max_arr[1]) + a
  max_tmp[1] = max(max_arr[0], max_arr[1], max_arr[2]) + b
  max_tmp[2] = max(max_arr[1], max_arr[2]) + c
  max_arr[0], max_arr[1], max_arr[2] = max_tmp[0], max_tmp[1], max_tmp[2]


print(max(max_arr), min(min_arr))