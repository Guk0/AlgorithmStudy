# https://www.acmicpc.net/problem/16926
# 배열 돌리기 1
# 구현


from sys import stdin

input = stdin.readline

N, M, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
  for i in range(min(N, M) // 2):
    x, y = i, i
    tmp1 = graph[x][y]

    for j in range(i+1, N-i):
      x = j
      tmp2 = graph[x][y]
      graph[x][y] = tmp1
      tmp1 = tmp2
        
    for j in range(i+1, M-i):
      y = j
      tmp2 = graph[x][y]
      graph[x][y] = tmp1
      tmp1 = tmp2
    
    for j in range(i+1, N-i):
      x = N-j-1
      tmp2 = graph[x][y]
      graph[x][y] = tmp1
      tmp1 = tmp2
                    
    for j in range(i+1, M-i):
      y = M-j-1
      tmp2 = graph[x][y]
      graph[x][y] = tmp1
      tmp1 = tmp2
                    
for i in range(N):
  for j in range(M):
    print(graph[i][j], end=' ')
  print()
