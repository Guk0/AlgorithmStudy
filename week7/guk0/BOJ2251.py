# https://www.acmicpc.net/problem/2251
# 물통
# DFS


from collections import deque

def bfs():
  visited = [[[False for _ in range(C+1)] for _ in range(B+1)] for _ in range(A+1)]
  stack = deque([])
  stack.append([0, 0, C])
  visited[0][0][C] = True
  answer = []
  while stack:
    a, b, c = stack.pop()
    if a == 0 and c not in answer:
      answer.append(c)

    if a != 0:
      tmp_b = min(B-b, a)
      tmp_c = min(C-c, a)
      if B - b != 0 and not visited[a-tmp_b][b+tmp_b][c]:
        visited[a-tmp_b][b+tmp_b][c] = True
        stack.append([a-tmp_b, b+tmp_b, c])
      if C - c != 0 and not visited[a-tmp_c][b][c+tmp_c]:
        visited[a-tmp_c][b][c+tmp_c] = True
        stack.append([a-tmp_c, b, c+tmp_c])

    if b != 0:
      tmp_a = min(A-a, b)
      tmp_c = min(C-c, b)
      if A - a != 0 and not visited[a+tmp_a][b-tmp_a][c]:
        visited[a+tmp_a][b-tmp_a][c] = True
        stack.append([a+tmp_a, b-tmp_a, c])
      if C - c != 0 and not visited[a][b-tmp_c][c+tmp_c]:
        visited[a][b-tmp_c][c+tmp_c]= True
        stack.append([a, b-tmp_c, c+tmp_c])

    if c != 0:
      tmp_a = min(A-a, c)
      tmp_b = min(B-b, c)
      if A - a != 0 and not visited[a+tmp_a][b][c-tmp_a]:
        stack.append([a+tmp_a, b, c-tmp_a])
        visited[a+tmp_a][b][c-tmp_a] = True
      if B - b != 0 and not visited[a][b+tmp_b][c-tmp_b]:
        visited[a][b+tmp_b][c-tmp_b] = True
        stack.append([a, b+tmp_b, c-tmp_b])


  return answer


A, B, C = map(int, input().split())
answer = bfs()
for el in sorted(answer):
  print(el, end=" ")

# 8 9 10

# 0 0 10 
# 0 9 1
# 8 1 1

# 1 5 8
# 3 7 5
