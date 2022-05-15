# https://www.acmicpc.net/problem/6987
# 월드컵
# 백트래킹

# 붙을 조합 뽑아놓고 승무패로 케이스 나눠서 돌려야함.


from itertools import combinations

def dfs(current):
  global possible
  if current == 15:
    if sum(sum(graph, [])) == 0:
      possible = True
    return
  
  x, y = combi[current]

  for i in range(3):
    if graph[x][i] != 0:
      if i == 0 or i == 2:
        target = 0 if i == 2 else 2
        if graph[y][target] != 0:
          graph[x][i] -= 1
          graph[y][target] -= 1
          dfs(current+1)
          graph[x][i] += 1
          graph[y][target] += 1
      else:            
        if graph[y][i] != 0:
          graph[x][i] -= 1
          graph[y][i] -= 1
          dfs(current+1)
          graph[x][i] += 1
          graph[y][i] += 1

combi = list(combinations(range(6), 2))
answer = []

for _ in range(4):
  arr = list(map(int, input().split()))
  graph = []
  matched = [[False for _ in range(6)] for _ in range(6)]
  possible = False
  for i in range(0, len(arr), 3):
    graph.append([arr[i], arr[i+1], arr[i+2]])

  dfs(0)
  answer.append(1 if possible else 0)
  
print(" ".join(map(str, answer)))
