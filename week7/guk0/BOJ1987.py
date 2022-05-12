# https://www.acmicpc.net/problem/1987
# 알파벳

from sys import stdin
from collections import deque


def bfs():
  queue = deque()
  previous = [False for _ in range(26)]
  answer = 0
  queue.append([[0, 0], previous, 0])

  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]  

  while queue:
    coordinate, visited, moved = queue.pop()    
    visited = visited[:]
    visited[ord(arr[coordinate[1]][coordinate[0]])-65] = True
    # visited.append(arr[coordinate[1]][coordinate[0]])
    answer = max(answer, moved+1)
    
    for i in range(4):
      nx = coordinate[0] + dx[i]
      ny = coordinate[1] + dy[i]
      if 0 <= nx < C and 0 <= ny < R and not visited[ord(arr[ny][nx])-65]:
        queue.append([[nx, ny], visited, moved+1])

  return answer



input = stdin.readline
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

print(bfs())