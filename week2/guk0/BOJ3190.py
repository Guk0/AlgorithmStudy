# https://www.acmicpc.net/problem/3190
# 뱀
# 구현 / 시뮬레이션 / 큐



from sys import stdin
from collections import deque

N = int(stdin.readline())
x, y = 1, 1
K = int(stdin.readline())
apples = [list(map(int, stdin.readline().split())) for _ in range(K)]
L = int(stdin.readline())
change_directions = [stdin.readline().split() for _ in range(L)]

queue = deque([[1, 1]])
cnt = 0
# D 오른쪽
# L 왼쪽

direction_arr = [[1, 0], [0, 1], [-1, 0], [0, -1]]
direction_index = 0
direction = []

while True:
  cnt += 1
  coordinate = direction_arr[direction_index]
  x, y = x+coordinate[0], y+coordinate[1]
  if [x, y] in queue or x < 1 or x > N or y < 1 or y > N:
    break
    
  queue.append([x, y])

  if [y, x] in apples:
    apples.remove([y, x])
  else:
    queue.popleft()

  if len(direction) == 0 and change_directions:
    direction = change_directions.pop(0)

  if direction and int(direction[0]) == cnt:
    # % 4 로 나누면 0~3 값만 나옴.
    if direction[1] == "D":
      direction_index = (direction_index+1) % 4
    else:
      direction_index = (direction_index-1) % 4

    # if direction[1] == "D":
    #   if direction_index == 3:
    #     direction_index = 0
    #   else:
    #     direction_index += 1
    # else:
    #   if direction_index == 0:
    #     direction_index = 3
    #   else:
    #     direction_index -= 1
        
    direction = []

    
print(cnt)