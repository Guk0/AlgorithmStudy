# https://www.acmicpc.net/problem/2263
# 트리의 순회

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def preorder(in_start, in_end, post_start, post_end):
  if in_end < in_start or post_end < post_start:
    return
    
  root = postorder[post_end]
  idx = position[root]
  
  result.append(root)

  preorder(in_start, idx-1, post_start, idx - in_start + post_start-1)
  preorder(idx+1, in_end, post_end - in_end + idx, post_end-1)


N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
result = []
position = [0] * (N+1)
for i in range(N):
  position[inorder[i]] = i

preorder(0, N-1, 0, N-1)

print(*result)




# 1 2 4 8 5 9 3 6 10 7 11




# 메모리 고려 전

# import sys
# sys.setrecursionlimit(10**5)
# input = sys.stdin.readline

# def preorder(inorder, postorder):
#   if not inorder:
#     return
#   root = postorder[-1]
#   idx = inorder.index(root)

#   result.append(root)
#   preorder(inorder[:idx], postorder[:idx])
#   preorder(inorder[idx+1:], postorder[idx:-1])


# N = int(input())
# inorder = list(map(int, input().split()))
# postorder = list(map(int, input().split()))
# result = []
# preorder(inorder, postorder)
# print(*result)




 

