# https://www.acmicpc.net/problem/4386
# 별자리 만들기
# 최소 스패닝 트리

import sys
import math
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

def get_distance(x, y):
  return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

N = int(input())
stars = [list(map(float, input().split())) for _ in range(N)]
edges = []
parent = [i for i in range(N)]
result = 0

for i in range(N):
  for j in range(i+1, N):
    distance = get_distance(stars[i], stars[j])
    edges.append((distance, i, j))

edges.sort()

for cost, a, b in edges:
  if find(a) != find(b):
    union(a, b)
    result += cost

print(round(result, 2))