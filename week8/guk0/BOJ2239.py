# https://www.acmicpc.net/problem/2239
# 스도쿠
# 백트래킹


from sys import stdin

input = stdin.readline

def dfs(cnt):
  if cnt == len(targets):
    for row in rows:
      print("".join(map(str, row)))
    exit(0)

  y, x = targets[cnt]
  for i in range(1, 10):
    if i not in rows[y] and i not in columns[x] and i not in section[(y//3)*3 + (x//3)]:
      rows[y][x] = i
      columns[x][y] = i
      section[(y//3)*3 + (x//3)][(y%3)*3 + (x%3)] = i
      dfs(cnt+1)
      rows[y][x] = 0
      columns[x][y] = 0
      section[(y//3)*3 + (x//3)][(y%3)*3 + (x%3)] = 0


rows = []
columns = [[] for _ in range(9)]
section = [[] for _ in range(9)]
targets = []

for i in range(9):
  arr = list(map(int, input().strip()))
  rows.append(arr)
  for j in range(9):
    columns[j].append(arr[j])
    section[(i//3)*3 + (j//3)].append(arr[j])
    if arr[j] == 0:
      targets.append([i, j])

dfs(0)


