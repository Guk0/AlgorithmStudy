# https://www.acmicpc.net/problem/9576
# 책 나눠주기
# 이분 매칭

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

T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  vector = [[]]
  dept = [0 for _ in range(N+1)]
  cnt = 0

  for i in range(M):
    start, end = map(int, input().split())
    vector.append(list(range(start, end+1)))
  
  for i in range(1, M+1):
    visited = [False for _ in range(N+1)]
    if dfs(i, visited): cnt += 1
  
  print(cnt)


