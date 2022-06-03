# https://www.acmicpc.net/problem/10830
# 행렬 제곱
# 분할 정복

from sys import stdin
input = stdin.readline


def multiply(arr1, arr2):
  n = len(arr1)
  result_arr = [[0]*n for _ in range(n)]
  
  for row in range(n):
    for col in range(n):
      e = 0
      for i in range(n):
        e += arr1[row][i] * arr2[i][col]
      result_arr[row][col] = e % 1000

  return result_arr

def square(arr, B):
  if B == 1:
    for x in range(len(arr)):
      for y in range(len(arr)):
        arr[x][y] %= 1000
    return arr
    
  tmp = square(arr, B//2)
  if B % 2:
    return multiply(multiply(tmp, tmp), arr)
  else:
    return multiply(tmp, tmp)


N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = square(arr, B)

for r in result:
  print(*r)
