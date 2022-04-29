# https://www.acmicpc.net/problem/11497
# 통나무 건너뛰기
# 그리디


# input을 역순으로 정렬하고 가운데 부터 차례대로 양쪽 끝으로 놓으면 차이가 최소
# 개수가 짝수인 경우도 동일
# i == 0 일때는 i+1과 i+2 비교
# i == N-2 즉 뒤에서 두번째 일 때 i+1과 비교
# 나머지는 i+2와 비교

# 10 11 12 13 12 11 10
# 4 7 9 5 2

from sys import stdin

input = stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  arr = list(map(int, input().split()))
  arr.sort(reverse=True)
  
  answer = arr[0] - arr[1]

  for i in range(N-1):
    if i == N-2:
      answer = max(arr[i] - arr[i+1], answer)
    else:
      answer = max(arr[i] - arr[i+2], answer)

  print(answer)