# https://www.acmicpc.net/problem/12851
# 숨바꼭질 2

from collections import deque

def bfs(N):
  queue = deque()
  queue.append(N)
  visited[N][0] = 0
  visited[N][1] = 1 

  while queue:
    current = queue.popleft()

    for i in [current - 1, current + 1, current * 2]:
      if 0 <= i <= 100000:
        if visited[i][0] == -1:
          visited[i][0] = visited[current][0] + 1
          visited[i][1] = visited[current][1]
          queue.append(i)
              
        elif visited[i][0] == visited[current][0] + 1:
          visited[i][1] += visited[current][1]


N, K = map(int, input().split())
visited = [[-1, 0] for _ in range(100001)]

bfs(N)
print(visited[K][0])
print(visited[K][1])
