# https://www.acmicpc.net/problem/1414
# 불우이웃돕기
# 최소 스패닝 트리

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(x):
  if parent[x] == x:
    return x
  
  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  rootX = find(x)
  rootY = find(y)

  if rootX > rootY:
    parent[rootX] = rootY    
  else:
    parent[rootY] = rootX
    


N = int(input())
alpabets = {}
for i in range(2):
  space = 96 if i == 0 else 64
  for j in range(1, 27):
    alpabets[chr(space+j)] = 26*i + j

graph = []
total_length = 0

for i in range(N):
  row = list(input())
  for j in range(N):
    if row[j] != "0":
      graph.append([alpabets[row[j]], i, j])
      total_length += alpabets[row[j]]

parent = [i for i in range(N)]
result = 0

graph.sort()
linked_len = 0

for length, y, x in graph:
  if find(y) != find(x):
    union(x, y)
    result += length
    linked_len += 1

if linked_len == N-1:
  print(total_length - result)
else:
  print(-1)