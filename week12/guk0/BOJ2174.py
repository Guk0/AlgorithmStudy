# https://www.acmicpc.net/problem/2174
# 로봇 시뮬레이션
# 구현, 시뮬레이션

from sys import stdin
input = stdin.readline

def do_order():
  for robot_idx, order, times in orders:
    robot_idx, times = int(robot_idx)-1, int(times)  

    if order == "L":
      for _ in range(times):
        index = directions.index(robot_direction[robot_idx])
        robot_direction[robot_idx] = directions[(index - 1 + 4) % 4]
    elif order == "R":
      for _ in range(times):
        index = directions.index(robot_direction[robot_idx])
        robot_direction[robot_idx] = directions[(index + 1) % 4]
    else:
      coordinate = direction_coordinate[robot_direction[robot_idx]]
      y, x = coordinate
      for _ in range(times):
        r_y, r_x = robots[robot_idx]
        if 0 <= r_y+y < B and 0 <= r_x+x < A:
            if graph[r_y+y][r_x+x] != 0:
              return "Robot {} crashes into robot {}".format(robot_idx+1, graph[r_y+y][r_x+x])
            graph[r_y][r_x] = 0
            graph[r_y+y][r_x+x] = robot_idx+1
            robots[robot_idx] = [r_y+y, r_x+x]
        else:
          return "Robot {} crashes into the wall".format(robot_idx+1)

  return "OK"


A, B = map(int, input().split()) # X, Y 순
N, M = map(int, input().split())
graph = [[0 for _ in range(A)] for _ in range(B)]
directions = ["N", "E", "S", "W"]
direction_coordinate = {"N": [1, 0], "E": [0, 1], "S": [-1, 0], "W": [0, -1]}
# N과 S 방향을 뒤집어야함. 문제 사진 참조
robot_direction = []
robots = []

for i in range(N):
  x, y, direction = input().split()
  y, x = int(y), int(x)
  robots.append([y-1, x-1])
  graph[y-1][x-1] = i+1
  robot_direction.append(direction)

orders = [input().split() for _ in range(M)]

print(do_order())