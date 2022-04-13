# https://www.acmicpc.net/problem/14428
# 수열과 쿼리 16
# 세그먼트 트리

from sys import stdin
import math

def check_index(x, y):
  if x == -1:
    return y;
  if y == -1:
    return x;

  if arr[x] == arr[y]:
    return x if x < y else y
  return x if arr[x] < arr[y] else y

def init(start, end, node):
  if start == end:
    tree[node] = start
    return tree[node]
  else:
    mid = (start + end) // 2
    tree[node] = check_index(init(start, mid, node*2), init(mid+1, end, node*2+1))
    return tree[node]


def update(start, end, node, index):
  if index < start or index > end or start == end:
    return tree[node]
  else:
    mid = (start + end) // 2
    tree[node] = check_index(update(start, mid, node*2, index), update(mid+1, end, node*2+1, index))
    return tree[node]

def query(start, end, node, section_start, section_end):  
  if start > section_end or end < section_start:
     return -1;
  elif section_start <= start and end <= section_end:
    return tree[node]
  else:
    mid = (start + end) // 2
    return check_index(query(start, mid, node*2, section_start, section_end), query(mid+1, end, node*2+1, section_start, section_end))


input = stdin.readline
N = int(input())
arr = list(map(int, input().split()))
M = int(input())

tree = [0] * 2 ** math.ceil(math.log2(N) + 1)
init(0, N-1, 1)

for _ in range(M):
  q = list(map(int, input().split()))
  if q[0] == 1:
    arr[q[1]-1] = q[2]
    update(0, N-1, 1, q[1]-1)
  else:
    print(query(0, N-1, 1, q[1]-1, q[2]-1)+1)
