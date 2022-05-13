# https://www.acmicpc.net/problem/1941
# 소문난 칠공주
# 백트래킹

# 선택 후 선택한 것들 전부 다시 for 루프 돌려서 4방향, 즉 ny, nx 방면으로
# 다시 dfs 재귀 함수 호출
# 5*5 배열은 0~24까지 int로 관리. visited에 길이 7인 이 int 배열 저장

def dfs(picked, S, Y):
  global visited, answer, arr
  if Y >= 4 or len(picked) > 7:
    return

  if len(picked) == 7 and S >= 4:    
    picked = tuple(sorted(picked))
    if picked not in visited:
      answer += 1
      visited.add(picked)
    return  # 7 도달하면 무조건 return하게 해야함.

  dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]

  for pos in picked:
    for i in range(4):
      ny = (pos // 5) + dy[i]
      nx = (pos % 5) + dx[i]
      n = ny * 5 + nx      
      if 0 <= ny < 5 and 0 <= nx < 5 and n not in picked:
        picked.append(n)
        dfs(
          picked, 
          S + 1 if arr[ny][nx] == "S" else S,
          Y + 1 if arr[ny][nx] == "Y" else Y
        )
        picked.pop()


from sys import stdin

input = stdin.readline

arr = [list(input().strip()) for _ in range(5)]
visited = set()
answer = 0

for i in range(5):
  for j in range(5):
    if arr[i][j] == "S":
      dfs([i*5 + j], 1, 0)

print(answer)

