# https://www.acmicpc.net/problem/1038
# 감소하는 수
# 백트래킹

# 1~9
# 10
# 20
# 21
# 30
# 31
# 32
# 40
# 41
# 42


# 987,654,321,0

# length가 11이상이면 감소하는 수가 되지 못함. 들어갈 수 있는 수가 0~9(10개) 이므로.
# 0부터 while 문을 돌면서 X에 1을 더하는 방식으로 구하면 너무 느림. 0~9까지 dfs 함수로 탐색하는게 제일 빠름
# 감소하는 수면 마지막 자리 다음 수가 마지막 자리보다 작아야 하므로 마지막 자리보다 작은 int만 재귀 탐색함.


def dfs(number):
  answer.append(int(number))

  for i in range(int(number[-1])):
    dfs(number + str(i))

N = int(input())

answer = []

for i in range(10):
  dfs(str(i))

answer.sort()
if len(answer) > N:
  print(sorted(answer)[N])
else:
  print(-1)