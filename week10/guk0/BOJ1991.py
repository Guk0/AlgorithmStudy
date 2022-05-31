# https://www.acmicpc.net/problem/1991
# 트리 순회

from sys import stdin
input = stdin.readline

def preorder(current):  
  global preorder_result

  preorder_result += current
  if tree[current][0] != ".":
    preorder(tree[current][0])
  if tree[current][1] != ".":
    preorder(tree[current][1])


def inorder(current):  
  global inorder_result

  if tree[current][0] != ".":
    inorder(tree[current][0])
  inorder_result += current
  if tree[current][1] != ".":
    inorder(tree[current][1])

def postorder(current):  
  global postorder_result

  if tree[current][0] != ".":
    postorder(tree[current][0])
  if tree[current][1] != ".":
    postorder(tree[current][1])
  postorder_result += current    

N = int(input())
tree = {chr(i+65): [] for i in range(N)}
preorder_result = ""
inorder_result = ""
postorder_result = ""

for _ in range(N):
  node, left, right = input().split()
  tree[node] = [left, right]

preorder("A")
inorder("A")
postorder("A")

print(preorder_result)
print(inorder_result)
print(postorder_result)