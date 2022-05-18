# https://www.acmicpc.net/problem/1967
# 트리의 지름
# dfs


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
  global result 
  max_value = 0
  max_weight = 0

  for x in graph[node]:
    m = dfs(x[0]) + x[1]
    max_value = max(max_value, max_weight+m)
    max_weight = max(max_weight, m)

  result = max(result, max_value)
  return max_weight



n = int(input())
graph = [[] for _ in range(n)]

for _ in range(n-1):
  a, b, w = map(int, input().split())
  graph[a-1].append([b-1, w])

result = 0

dfs(0)
print(result)