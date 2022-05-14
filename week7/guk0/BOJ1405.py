# https://www.acmicpc.net/problem/1405
# 미친 로봇
# 백트래킹


# 동서남북(EWSN)
# 나중에 ENWSSSEE 경로에 각 확률을 곱함. 전부 25일때는 0.25*0.25*0.25*0.25 ... 이런 식으로
# 나중에 단순하지 않는 경로를 토탈에 안 더함
# 지나간 경로를 다시 지나면 안됨
# visited는 DFS이므로 dfs 함수 호출하기 전 True하고 호출 다음에 False로 바꿔줌

def dfs(route, percentage, coordinate):
  global total
  if len(route) == N:
    total += percentage
    return

  for i in range(4):
    x, y = coordinate[0] + distance[i][0], coordinate[1] + distance[i][1]
    if percentages[i] != 0 and not visited[y][x]:
      visited[y][x] = True
      dfs(route+direction[i], percentages[i] * percentage, [x, y])
      visited[y][x] = False


N, *percentages = map(int, input().split())
percentages = list(map(lambda x: x/100, percentages))
direction = ["E", "W", "S", "N"]
distance = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = [[False for _ in range(28)] for _ in range(28)]
visited[13][13] = True
total = 0


dfs("", 1, [13, 13])

print(total)