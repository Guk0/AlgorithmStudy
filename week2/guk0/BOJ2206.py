# https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기
# bfs

# visited 배열을 3차원으로 놓고 풀어야함. visitied[y][x][z].
# z는 0 아니면 1이고
# 0일때는 벽을 안부시고 온 경우 이동한 거리
# 1일때는 벽을 부시고 왔을 경우 이동한 거리
# z를 0과 1로 두어 각 경우에 대해 방문한지 안 한지를 다르게 체크.

# 단순히 2차원으로 놓을 경우 벽을 만나면 무조건 부수는 경우만 생각하므로 벽을 
# 안부수고 온 경우에 이미 부수고 온 경우에 의해 visitied 체크에 걸려버림

# 아래는 2차원 배열에 대한 반례

# 반례
# 01000
# 00110
# 10110
# 00111
# 01111
# 01000


def bfs():
  queue = deque()
  queue.append([0, 0, 0])
  visited[0][0][0] = 1
  

  while queue:
    y, x, z = queue.popleft()
    if y == N-1 and x == M-1:
      return visited[y][x][z]

    for i in range(4):
      ny = dy[i] + y
      nx = dx[i] + x

      if 0 <= ny <= N-1 and 0 <= nx <= M-1:
        # visited[ny][nx][z]에 이전 노드(visited[y][x][z] 값 + 1을 함. (이동한 거리))
        # visited[ny][nx][z] == 0이라는 조건은 이 노드를 방문한 적이 없다는 뜻.
        if graph[ny][nx] == 0 and visited[ny][nx][z] == 0:
          queue.append([ny, nx, z])
          visited[ny][nx][z] = visited[y][x][z] + 1

        elif graph[ny][nx] == 1 and z == 0:
          queue.append([ny, nx, 1])
          visited[ny][nx][1] = visited[y][x][0] + 1

  return -1


import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

print(bfs())





# 3차원 visited 배열을 사용하지 않았을 때의 반례.
# 아래 코드는 벽을 만나면 무조건 부심

# 반례
# 01000
# 00110
# 10110
# 00111
# 01111
# 01000

# -1을 return 함

# def bfs():
#   queue = deque()
#   queue.append([0, 0, False, 1])
#   visited[0][0] = True
  

#   while queue:
#     y, x, is_break, cnt = queue.popleft()
#     for i in range(4):
#       ny = dy[i] + y
#       nx = dx[i] + x
#       if ny == N-1 and nx == M-1:
#         return cnt+1

#       if 0 <= ny <= N-1 and 0 <= nx <= M-1 and not visited[ny][nx]:
#         if graph[ny][nx] == 1 and not is_break:
#           queue.append([ny, nx, True, cnt+1])
#           visited[ny][nx] = True

#         if graph[ny][nx] == 0:
#           queue.append([ny, nx, is_break, cnt+1])
#           visited[ny][nx] = True

#   return -1


# import sys
# from collections import deque

# input = sys.stdin.readline

# N, M = map(int, input().split())

# graph = [list(map(int, input().strip())) for _ in range(N)]
# visited = [[False for _ in range(M)] for _ in range(N)]
# dy = [1, 0, -1, 0]
# dx = [0, 1, 0, -1]

# print(bfs())

