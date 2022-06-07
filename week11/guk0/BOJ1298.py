# https://www.acmicpc.net/problem/1298
# 노트북의 주인을 찾아서


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(current, visited):
  for el in vector[current]:
    if not visited[el]:
      visited[el] = True
      if dept[el] == 0 or dfs(dept[el], visited):
        dept[el] = current
        return True
  return False


N, M = map(int, input().split())
vector = [[] for _ in range(N+1)]
dept = [0 for _ in range(N+1)]
cnt = 0

for _ in range(M):
  a, b = map(int, input().split())
  vector[a].append(b)

for i in range(1, N+1):
  visited = [False for _ in range(N+1)]
  if dfs(i, visited): cnt += 1

print(cnt)