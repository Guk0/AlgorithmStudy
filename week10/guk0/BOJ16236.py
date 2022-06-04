# https://www.acmicpc.net/problem/16236
# 아기 상어
# bfs, 시뮬레이션

# dy, dx로 queue에 append되는 순서를 조절하므로써 우선순위를 줄 수 없다.
# 가능한 모든 가장 짧은 거리 pos를 얻은 후 min 때려야함

# 인접한 상하좌우로 움직임

# 자신의 크기보다 큰 물고기가 있는 칸은 지날 수 없음
# 나머지 칸은 지나갈 수 있음.
# 자신의 크기보다 작은 물고기만 먹을 수 있음.
# 크기가 같다면 먹을 수 없지만 지날 수 있음.

# 가장 가까운 물고기를 먹으러감. 지나야하는 칸의 개수의 최솟값
# 가장 가까운 물고기가 많다면 가장 위에 물고기를 먹으러감. 여러마리면 가장 왼쪽에 있는 물고기를 먹음

# 자신의 크기와 같은 수의 물고기를 먹을때마다 크기가 1증가. 
# 2인 아기상어는 물고기 2마리 먹으면 크기 3

# 초기 아기상어의 크기는 2


from sys import stdin
from collections import deque
input = stdin.readline

def bfs(shark_pos):
  global shark_size
  
  queue = deque()
  queue.append([*shark_pos, 0])
  visited = [[False for _ in range(N)] for _ in range(N)]
  visited[shark_pos[0]][shark_pos[1]] = True
  dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]
  target_distance = -1
  target_arr = []
  while queue:
    y, x, distance = queue.popleft()
    if graph[y][x] != 0 and graph[y][x] < shark_size:
      if target_distance == -1:
        target_distance = distance
        target_arr.append([y, x])
      elif target_distance == distance:
        target_arr.append([y, x])


    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]
      if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and shark_size >= graph[ny][nx]:
        if (target_distance == -1) or (target_distance == distance):
          queue.append([ny, nx, distance+1])
          visited[ny][nx] = True

  return [target_arr, target_distance]


N = int(input())
graph = []
fishes = []
shark_pos = []
shark_size = 2
eat_cnt = 0

for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(N):
    if graph[i][j] not in (0, 9):
      fishes.append([i, j])
    elif graph[i][j] == 9:
      shark_pos = [i, j]

cnt = 0

while True:
  positions, distance = bfs(shark_pos)
  if not positions:
    break

  y, x = min(positions)
  graph[shark_pos[0]][shark_pos[1]] = 0
  graph[y][x] = 9
  eat_cnt += 1
  cnt += distance
  shark_pos = [y, x]

  if shark_size < 7 and eat_cnt == shark_size:
    eat_cnt = 0
    shark_size += 1

print(cnt)