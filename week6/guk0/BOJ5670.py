# https://www.acmicpc.net/problem/5670
# 휴대용 자판
# 트라이

import sys
 
class Node:
  def __init__(self, chr):
    self.chr = chr
    self.children = {}
    self.check = False
 
class Trie:
  def __init__(self):
    self.root = Node('')

  
  def insert(self, word):
    node = self.root
    for char in word:
      if char not in node.children:
        new = Node(char)
        node.children[char] = new
        node = new
      else:
        node = node.children[char]
    node.check = True

  
  def search(self, word):
    node = self.root

    cnt = 0    
    for char in word:
      node = node.children[char]
      if len(node.children) > 1 or node.check:
        cnt += 1
    return cnt
 
while True:
  trie = Trie()
  words = []
  
  try:n = int(sys.stdin.readline())
  except:break

  for _ in range(n):
    s = sys.stdin.readline().rstrip()
    trie.insert(s)
    words.append(s)
  result = 0

  for word in words:
    result += trie.search(word)

  print("%.2f" % (result/n))