# https://www.acmicpc.net/problem/1080
# 행렬

from sys import stdin

def reverse(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
          from_arr[i][j] = 1 - from_arr[i][j]

def check():
  for i in range(N):
    for j in range(M):
      if from_arr[i][j] != to_arr[i][j]:
        return False
  
  return True

input = stdin.readline

N, M = map(int, input().split())

from_arr = [list(map(int, list(input().strip()))) for _ in range(N)]
to_arr = [list(map(int, list(input().strip()))) for _ in range(N)]

cnt = 0

for i in range(N-2):
  for j in range(M-2):
    if from_arr[i][j] != to_arr[i][j]:
      reverse(i, j)
      cnt += 1

if check():
  print(cnt)
else:
  print("-1")
