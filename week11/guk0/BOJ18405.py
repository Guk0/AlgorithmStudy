# https://www.acmicpc.net/problem/18405
# 경쟁적 전염
# BFS, 시뮬레이션

from sys import stdin
from collections import deque
input = stdin.readline

def spread_viruses():
  queue = deque()
  for el in viruses:
    queue.append(el)

  while queue:
    k, cnt, y, x = queue.popleft()
    if cnt >= S:
      break
    for i in range(4):
      ny, nx = dy[i] + y, dx[i] + x
      if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and graph[ny][nx] == 0:
        visited[ny][nx] = True
        queue.append([k, cnt+1, ny, nx])
        graph[ny][nx] = k

N, K = map(int, input().split())
viruses = []
graph = []
visited = [[False for _ in range(N)] for _ in range(N)]
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

for i in range(N):
  arr = list(map(int, input().split()))
  graph.append(arr)
  for j in range(N):
    if arr[j] > 0:
      viruses.append([arr[j], 0, i, j])
      visited[i][j] == True

viruses.sort()
S, Y, X = map(int, input().split())

spread_viruses()
  
print(graph[Y-1][X-1])