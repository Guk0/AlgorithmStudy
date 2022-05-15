# https://www.acmicpc.net/problem/2580
# 스도쿠
# 백트래킹


from sys import stdin

input = stdin.readline


def dfs(current): 
  if current == len(empty):
    for el in rows:
      print(" ".join(map(str, el)))
    exit()

  y, x = empty[current]

  for k in range(1, 10):
    if k not in rows[y] and k not in columns[x] and k not in squares[(y//3)*3 + x//3]:
      rows[y][x] = k
      columns[x][y] = k
      squares[(y//3)*3 + x//3][(y%3)*3 + x%3] = k
      dfs(current+1)
      rows[y][x] = 0
      columns[x][y] = 0
      squares[(y//3)*3 + x//3][(y%3)*3 + x%3] = 0


rows = [list(map(int, input().split())) for _ in range(9)]
columns = [[] for _ in range(9)] # 세로
squares = [[] for _ in range(9)] # 3*3 사각형, 3으로 나눈 몫
empty = []

for i in range(9):
  for j in range(9):
    columns[j].append(rows[i][j])
    squares[(i//3)*3 + j//3].append(rows[i][j])
    if rows[i][j] == 0:
      empty.append([i, j])

dfs(0)

