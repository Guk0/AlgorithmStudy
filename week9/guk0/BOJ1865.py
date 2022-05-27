# https://www.acmicpc.net/problem/1865
# 웜홀
# 벨만 포드

# 음수사이클이 존재하는지만 확인하면 됨. 

# distance[e] != inf 조건이 빠짐. 
# 해당 조건은 시작지점부터 연결된 노드를 찾기 위함인데
# distance는 시작지점으로부터의 최단 거리 테이블이라는 원래 의미를 갖지 않게 된다

from sys import stdin
input = stdin.readline

def bf(start):
  distance = [inf] * (N + 1)
  distance[start] = 0
  for i in range(1, N+1):
    for s, e, w in edges:
      if distance[e] > distance[s] + w:
        distance[e] = distance[s] + w
        if i == N:
          return "YES"

  return "NO"


TC = int(input())
inf = int(10e9)

for _ in range(TC):
  N, M, W = map(int, input().split())
  edges = []

  for _ in range(M):
    s, e, t = map(int, input().split())
    edges.append([s, e, t])
    edges.append([e, s, t])

  for _ in range(W):
    s, e, t = map(int, input().split())
    edges.append([s, e, -t])


  print(bf(1))


