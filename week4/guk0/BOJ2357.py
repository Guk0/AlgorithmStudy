# https://www.acmicpc.net/problem/2357
# 최솟값과 최댓값
# 세그먼트 트리

from sys import stdin
import math

def min_init(start, end, node):
  if start == end:
    min_tree[node] = arr[start]
    return min_tree[node]
  else:
    mid = (start + end) // 2
    min_tree[node] = min(min_init(start, mid, node*2), min_init(mid+1, end, node*2+1))
    return min_tree[node]

def max_init(start, end, node):
  if start == end:
    max_tree[node] = arr[start]
    return max_tree[node]
  else:
    mid = (start + end) // 2
    max_tree[node] = max(max_init(start, mid, node*2), max_init(mid+1, end, node*2+1))
    return max_tree[node]


def min_query(start, end, node, left, right):
  if left > end or right < start:
    return INF
  elif left <= start and right >= end:
    return min_tree[node]
  else:
    mid = (start + end) // 2
    return min(min_query(start, mid, node*2, left, right), min_query(mid+1, end, node*2+1, left, right))


def max_query(start, end, node, left, right):
  if left > end or right < start:
    return -1
  elif left <= start and right >= end:
    return max_tree[node]
  else:
    mid = (start + end) // 2
    return max(max_query(start, mid, node*2, left, right), max_query(mid+1, end, node*2+1, left, right))


input = stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
min_tree = [0] * 2 ** math.ceil(math.log2(N) + 1)
max_tree = [0] * 2 ** math.ceil(math.log2(N) + 1)
min_init(0, N-1, 1)
max_init(0, N-1, 1)
INF = 1e9

for _ in range(M):
  a, b = map(int, input().split())
  print(min_query(0, N-1, 1, a-1, b-1), max_query(0, N-1, 1, a-1, b-1))