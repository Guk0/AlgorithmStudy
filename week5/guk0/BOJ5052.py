# https://www.acmicpc.net/problem/5052
# 전화번호 목록
# trie

from sys import stdin

class Node(object):
  def __init__(self, key, data=None):
    self.key = key
    self.data = data
    self.children = {}


class Trie(object):
  def __init__(self):
    self.head = Node(None)

  def insert(self, string):
    curr_node = self.head
    for char in string:
      if char not in curr_node.children:
        curr_node.children[char] = Node(char)
      curr_node = curr_node.children[char]
    curr_node.data = string


  def search(self, string):
    curr_node = self.head

    for char in string:
      curr_node = curr_node.children[char]
    if curr_node.children:
      return False
    else:
      return True


T = int(stdin.readline())

for _ in range(T):
  N = int(stdin.readline())
  trie = Trie()
  arr = []
  for _ in range(N):
    num = stdin.readline().strip()
    arr.append(num)
    trie.insert(num)
 
  flag = True
  arr.sort()
  for num in arr:
    if not trie.search(num):
      flag = False
      break
  
  if flag:
    print("YES")
  else:
    print("NO")


