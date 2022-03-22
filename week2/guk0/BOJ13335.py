# https://www.acmicpc.net/problem/13335
# 트럭
# 구현/시뮬레이션

# queue를 만들어 while 문을 돌림. 매 반복마다 popleft를 먼저 한 뒤
# 조건에 따라 차 또는 0을 append함

from collections import deque

N, W, L = map(int, input().split()) # 트럭수, 다리 길이, 최대 하중
arr = list(map(int, input().split()))

queue = deque([0] * W)
result = 0

while queue:
  queue.popleft()
  result += 1

  if len(arr) > 0:
    if sum(queue, arr[0]) <= L and len(queue) < W:
      queue.append(arr[0])
      arr.pop(0)
    else:
      queue.append(0)

print(result)