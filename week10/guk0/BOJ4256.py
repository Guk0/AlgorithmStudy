# https://www.acmicpc.net/problem/4256
# 트리

def postorder(preorder, inorder):
  if len(preorder) == 0:
    return

  if len(preorder) == 1:
    result.extend(preorder)
    return
      
  root = preorder[0]
  inorder_index = inorder.index(root)
  
  postorder(preorder[1:inorder_index+1], inorder[:inorder_index])
  postorder(preorder[inorder_index+1:], inorder[inorder_index+1:])
  result.append(root)

from sys import stdin
input = stdin.readline
 
T = int(input())
for _ in range(T):
  N = int(input())  
  preorder = list(map(int, input().split()))
  inorder = list(map(int, input().split()))
  result = []  
  postorder(preorder, inorder)
  print(*result)



