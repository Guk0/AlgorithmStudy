# https://www.acmicpc.net/problem/17609
# 회문

from sys import stdin
input = stdin.readline

def is_palindrome(string):
  p1 = 0
  p2 = len(string) - 1

  while p1 < p2:
    if string[p1] == string[p2]:
      p1 += 1
      p2 -= 1
    else:
      tmp1 = string[:p1] + string[p1 + 1:]
      tmp2 = string[:p2] + string[p2 + 1:]
      
      if tmp1[:] == tmp1[::-1] or tmp2[:] == tmp2[::-1]:
        return 1        
      else:
        return 2
  return 0


T = int(input())

for _ in range(T):
  string = input().strip()
  print(is_palindrome(string))

  