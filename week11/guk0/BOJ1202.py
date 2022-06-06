# https://www.acmicpc.net/problem/1202
# 보석 도둑

import heapq
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
jewels.sort()
bags.sort()

queue = []
result = 0
for bag in bags:
  while jewels and bag >= jewels[0][0]:
    heapq.heappush(queue, -jewels[0][1])
    heapq.heappop(jewels)

  if queue:
    result -= heapq.heappop(queue)
  elif not jewels:
    break

print(result)
# 5 100
# 7 50

# 10
# 6