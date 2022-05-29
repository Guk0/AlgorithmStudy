# https://www.acmicpc.net/problem/2887
# 행성 터널
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
planets = [[i] + list(map(int, input().split())) for i in range(N)]
edges = []
parent = [i for i in range(N)]
result = 0

x = sorted(planets, key=lambda x: x[1])
y = sorted(planets, key=lambda x: x[2])
z = sorted(planets, key=lambda x: x[3])

for i in range(1, N):
  edges.append((abs(x[i-1][1] - x[i][1]), x[i-1][0], x[i][0]))
  edges.append((abs(y[i-1][2] - y[i][2]), y[i-1][0], y[i][0]))
  edges.append((abs(z[i-1][3] - z[i][3]), z[i-1][0], z[i][0]))

edges.sort()

for cost, a, b in edges:
  if find(a) != find(b):
    union(a, b)
    result += cost

print(result)