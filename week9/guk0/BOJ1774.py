# https://www.acmicpc.net/problem/1774
# 우주신과의 교감
# 최소 스패닝 트리

import sys
import math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def get_distance(x, y):
  return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def find(x):
  if parent[x] == x:
    return x

  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  rootX = find(x)
  rootY = find(y)

  if rootX < rootY:
    parent[rootY] = rootX
  else:
    parent[rootX] = rootY

N, M = map(int, input().split())

edges = []
parent = [i for i in range(N)]
gods = [list(map(int, input().split())) for _ in range(N)]
result = 0

for _ in range(M):
  a, b = map(int, input().split())
  union(a-1, b-1)

for i in range(N):
  for j in range(i+1, N):
    edges.append((get_distance(gods[i], gods[j]), i, j))

edges.sort()

for cost, a, b in edges:
  if find(a) != find(b):
    union(a, b)
    result += cost

print(format(result,".2f"))