# https://www.acmicpc.net/problem/16953
# A -> B
# 그리디


def solution(A, B):
  answer = 1

  while True:
    if B == A:
      return answer

    if B < A:
      return -1

    if B % 2 == 0:
      B = B // 2
      answer += 1
    elif str(B)[-1] == "1":
      B = int(str(B)[:-1])
      answer += 1
    else:
      return -1


A, B = map(int, input().split())
print(solution(A, B))
