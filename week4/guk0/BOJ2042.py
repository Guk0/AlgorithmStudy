# https://www.acmicpc.net/problem/2042
# 구간 합 구하기
# 세그먼트 트리

import math
from sys import stdin


def init(start, end, node):
  if start == end:
    tree[node] = arr[start]
    return tree[node]
  else:
    mid = (start + end) // 2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node]

def update(start, end, node, index):
  if index < start or index > end:
    return tree[node]
  elif start == end:
    tree[node] = arr[start]
    return tree[node]
  else:
    mid = (start + end) // 2
    tree[node] = update(start, mid, node*2, index) + update(mid+1, end, node*2+1, index)
    return tree[node]

def query(start, end, node, left, right):
  if left > end or right < start:
    return 0
  elif left <= start and right >= end:
    return tree[node]
  else:
    mid = (start + end) // 2    
    return query(start, mid, node*2, left, right) + query(mid+1, end, node*2+1, left, right)



input = stdin.readline

N, M, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]

tree = [0] * 2 ** math.ceil(math.log2(N) + 1)
init(0, N-1, 1)

for _ in range(M + K):
  a, b, c = map(int, input().split())
  if a == 1:
    arr[b-1] = c
    update(0, N-1, 1, b-1)
  else:    
    print(query(0, N-1, 1, b-1, c-1))