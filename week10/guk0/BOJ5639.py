# https://www.acmicpc.net/problem/5639
# 이진 검색 트리

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def postorder(start, end):
  if start > end:
    return

  idx = end+1

  for i in range(start+1, end+1):
    if preorder[start] < preorder[i]:
      idx = i
      break
  
  postorder(start+1, idx-1)
  postorder(idx, end)
  print(preorder[start])

preorder = []

while True:
  try:
    temp = int(input())
  except:
    break
  preorder.append(temp)

postorder(0, len(preorder)-1)



# 50, 30, 24, 5, 28, 45, 98, 52, 60

#          50
#     30        98
#  24    45   52
# 5  28         60