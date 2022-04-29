# https://www.acmicpc.net/problem/1946
# 신입 사원
# 그리디

# 하나 정렬 해놓고 나머지 한 과목만 비교. max_grade보다 작은 등수 있을 시 선발. 
# max_grade 보다 등수가 크면 탈락.

from sys import stdin

input = stdin.readline

N = int(input())

for _ in range(N):
  M = int(input())
  arr = [list(map(int, input().split())) for _ in range(M)]
  arr.sort()

  max_grade = arr[0][1]
  answer = 1

  for el in arr[1:]:
    if max_grade > el[1]:
      max_grade = el[1]
      answer += 1


  print(answer)
  