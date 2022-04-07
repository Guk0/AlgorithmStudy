# https://www.acmicpc.net/problem/14427
# 수열과 쿼리 15
# 세그먼트 트리

import math
from sys import stdin

def min_index(x, y):
  if arr[x] == arr[y]:
    return x if x < y else y
  return x if arr[x] < arr[y] else y

def init(left, right, node):
  if left == right:
    tree[node] = left
    return tree[node]
  else:
    mid = (left + right) // 2
    tree[node] = min_index(init(left, mid, node*2), init(mid+1, right, node*2+1))
    return tree[node]

def update(left, right, node, idx):
  if idx < left or idx > right or left == right:
    return tree[node]  
  else:
    mid = (left + right) // 2        
    tree[node] = min_index(update(left, mid, node*2, idx), update(mid+1, right, node*2+1, idx))
    return tree[node]

input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

 
tree = [0] * 2 ** math.ceil(math.log2(N) + 1)
init(0, N-1, 1)
for i in range(M):
  query = list(map(int, input().split()))
  if query[0] == 1:
    arr[query[1]-1] = query[2];
    update(0, N-1, 1, query[1]-1)
  else:
    print(tree[1]+1)
