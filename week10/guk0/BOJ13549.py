# https://www.acmicpc.net/problem/13549
# 숨바꼭질

import heapq

def bfs(start, end):
  queue = []
  heapq.heappush(queue, [0, start])
  visited[start] = True

  while queue:
    time, node = heapq.heappop(queue)
    
    if node == end:
      return time

    if 0 <= node*2 <= 100000 and not visited[node*2]:
      visited[node*2] = True
      heapq.heappush(queue, [time, node*2])

    if 0 <= node-1 <= 100000 and not visited[node-1]:
      visited[node-1] = True
      heapq.heappush(queue, [time+1, node-1])

    if 0 <= node+1 <= 100000 and not visited[node+1]:
      visited[node+1] = True
      heapq.heappush(queue, [time+1, node+1])


      
N, K = map(int, input().split())
visited = [False for _ in range(100001)]
print(bfs(N, K))