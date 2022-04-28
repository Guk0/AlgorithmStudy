# https://www.acmicpc.net/problem/15903
# 카드 합체 놀이
# 그리디, heapq(우선순위큐)


from sys import stdin
import heapq

queue = []
n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

for el in arr:
  heapq.heappush(queue, el)

for _ in range(m):
  popped1 = heapq.heappop(queue)
  popped2 = heapq.heappop(queue)
  heapq.heappush(queue, popped1 + popped2)
  heapq.heappush(queue, popped1 + popped2)

print(sum(queue))