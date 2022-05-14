# https://www.acmicpc.net/problem/3980
# 선발명단
# 백트래킹


from sys import stdin

def dfs(current, scores):
  if current == 11:
    total.append(scores)
    return

  for i in range(11):
    if arr[current][i] != 0 and not picked[i]:
      picked[i] = True
      dfs(current+1, scores+arr[current][i])
      picked[i] = False

input = stdin.readline
C = int(input())

for _ in range(C):
  arr = [list(map(int, input().split())) for _ in range(11)]
  picked = [False for _ in range(11)]
  total = []

  for i in range(11):
    if arr[0][i] != 0:
      picked[i] = True
      dfs(1, arr[0][i])
      picked[i] = False

  print(max(total))