# https://www.acmicpc.net/problem/1922
# 네트워크 연결
# 최소 스패닝 트리

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

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

N = int(input())
M = int(input())

edges = []
result = 0
parent = [i for i in range(1, N+1)]
parent = [0] + parent

for _ in range(M):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))
edges.sort()

for cost, a, b in edges:
  if find(a) != find(b):
    union(a, b)
    result += cost

print(result)