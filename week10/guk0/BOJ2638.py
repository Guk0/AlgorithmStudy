# https://www.acmicpc.net/problem/2638
# 치즈


import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(y, x):
  for i in range(4):
    ny, nx = y + dy[i], x + dx[i]
    if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and graph[ny][nx] != 1:
      visited[ny][nx] = True
      graph[ny][nx] = 2
      dfs(ny, nx)
      

def bfs():
  global cheese_cnt

  stack = deque()
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 1:
        stack.append([i, j])
        visited[i][j] = True

  while stack:
    y, x = stack.pop()
    exterior_cnt = 0
    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]

      if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 2:
        exterior_cnt += 1
    
    if exterior_cnt >= 2:
      graph[y][x] = 0
      cheese_cnt -= 1


N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
cheese_cnt = 0
time = 0

for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      cheese_cnt += 1

while cheese_cnt > 0:
  # print(cheese_cnt)  
  time += 1
  visited = [[False for _ in range(M)] for _ in range(N)]
  graph[0][0] = 2
  dfs(0, 0)
  bfs()  


print(time)


