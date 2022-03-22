# https://www.acmicpc.net/problem/14503
# 로봇 청소기
# 구현 / 시뮬레이션

from sys import stdin

N, M = map(int, stdin.readline().split()) # 세로 N, 가로 M
r, c, d = map(int, stdin.readline().split()) # (r,c) 시작 좌표. d 바라보고 있는 방향
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

# r, c는 y, x 형태
y, x = r, c
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 북, 동, 남, 서
# 북 서 동 남 순으로 회전 d에 -1씩 더해준다.
result = 0
flag = True

while flag:
  if not visited[y][x]:
    visited[y][x] = True
    result += 1

  cnt = 0
  while True:
    cnt += 1
    d = (d-1) % 4
    coordinate = directions[d]
    tmp_y, tmp_x = y + coordinate[0], x + coordinate[1]
    if not visited[tmp_y][tmp_x] and graph[tmp_y][tmp_x] == 0:
      y, x = tmp_y, tmp_x
      break
    
    if cnt == 4:
      tmp_d = (d-2) % 4
      coordinate = directions[tmp_d]
      y, x = y + coordinate[0], x + coordinate[1]
      if graph[y][x] == 1:
        flag = False
      break

print(result)