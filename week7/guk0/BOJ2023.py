# https://www.acmicpc.net/problem/2023
# 신기한 소수
# 백트래킹

import math

def checkPrime(number):
  for i in range(2, math.floor(math.sqrt(number))+1):
    if number % i == 0:
      return False
  return True


def dfs(number):
  if len(number) == N:
    answer.append(int(number))
  
  for i in range(10):
    next_number = number + str(i)
    if checkPrime(int(next_number)):
      dfs(next_number)


N = int(input())
answer = []

for prime in ["2", "3", "5", "7"]:
  dfs(prime)

answer.sort()

for number in answer:
  print(number)