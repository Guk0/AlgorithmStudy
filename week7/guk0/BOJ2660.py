# https://www.acmicpc.net/problem/2660
# 회장뽑기
# 플로이드-워셜

# 어떤 노드와 친구 사이면 1. 어떤 노드와 친구의 친구 사이면 2. 어떤 노드와 친구의 친구의 친구 사이면 3.
# 친구의 친구 사이려면 A와 친구, 친구와 B의 값은 1이어야함. A와 B의 값이 inf라면 둘의 관계는 2가 됨(1이라면 그냥 1). 
# 그러므로 플로이드 워셜 써가지고 min() 값 구하면 됨

from sys import stdin

input = stdin.readline


N = int(input())
inf = int(10e9)
graph = [[inf for _ in range(N)] for _ in range(N)]

for i in range(N):
  for j in range(N):
    if i == j:
      graph[i][j] = 0

while True:
  a, b = map(int, input().split())
  if a == -1: 
    break  
  graph[a-1][b-1] = 1
  graph[b-1][a-1] = 1


for k in range(N):
  for i in range(N):
    for j in range(N):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

scores = list(map(max, graph))
min_score = min(scores)
answer = []
for i in range(len(scores)):
  if scores[i] == min_score:
    answer.append(i+1)


print(min_score, len(answer))
print(" ".join(map(str, answer)))