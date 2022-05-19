# https://www.acmicpc.net/problem/1967
# 트리의 지름
# dfs

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n)]

def dfs(x, weight):
  for i in graph[x]:
    a, b = i
    if distance[a] == -1:
      distance[a] = weight + b
      dfs(a, weight + b)


for _ in range(n - 1):
  a, b, c = map(int, input().split())
  graph[a-1].append([b-1, c])
  graph[b-1].append([a-1, c])

distance = [-1] * (n) 
distance[0] = 0
dfs(0, 0) # 1번 노드에서 가장 먼 곳


# 가장 먼 노드에서 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
distance = [-1] * (n)
distance[start] = 0
dfs(start, 0)

print(max(distance))



# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# def dfs(node):
#   global result 
#   max_value = 0
#   max_weight = 0

#   for x in graph[node]:
#     m = dfs(x[0]) + x[1]
#     max_value = max(max_value, max_weight+m)
#     max_weight = max(max_weight, m)

#   result = max(result, max_value)
#   return max_weight



# n = int(input())
# graph = [[] for _ in range(n)]

# for _ in range(n-1):
#   a, b, w = map(int, input().split())
#   graph[a-1].append([b-1, w])

# result = 0

# dfs(0)
# print(result)