# https://www.acmicpc.net/problem/3665
# 최종 순위
# 위상 정렬


# 큐에 el이 두개 이상 존재하면 순서를 매길 수 없음. 
# 순서가 보장되려면 진입차수가 등수 순으로 0부터 N-1까지 오름차순으로 되어있어야함.

from sys import stdin
from collections import deque
input = stdin.readline

def topology_sort():
  global is_impossible
  queue = deque()
  for i in range(1, N+1):
    if in_degree[i] == 0:
      queue.append(i)
  
  while queue:
    if len(queue) > 1:
      is_impossible = True
      return

    node = queue.popleft()
    result.append(node)
    for next_node in graph[node]:
      in_degree[next_node] -= 1
      if in_degree[next_node] == 0:
        queue.append(next_node)
      elif in_degree[next_node] < 0:
        is_impossible = True
        return

  if sum(in_degree) > 0:
    is_impossible = True

T = int(input())

for _ in range(T):
  N = int(input())
  previous = [0] + list(map(int, input().split()))
  M = int(input())
  graph = [[] for _ in range(N+1)]
  in_degree = [0 for _ in range(N+1)]
  result = []
  is_impossible = False

  for i in range(1, N):
    arr = previous[i+1:]
    graph[previous[i]] = arr
    for el in arr:
      in_degree[el] += 1


  for _ in range(M):
    X, Y = map(int, input().split())
    if Y in graph[X]:
      graph[X].remove(Y)
      in_degree[Y] -= 1
      graph[Y].append(X)
      in_degree[X] += 1
    else:
      graph[X].append(Y)
      graph[Y].remove(X)
      in_degree[X] -= 1
      in_degree[Y] += 1

  topology_sort()

  if is_impossible:
    print("IMPOSSIBLE")
  else:
    print(*result)

  