# https://www.acmicpc.net/problem/2661
# 좋은수열
# 백트래킹


# 11, 1212, 123123, 12131213 .... 같으면 안된다.
#   for i in range(1, (index//2) + 1):
#     if sequence[-i:] == sequence[-2*i:-i]: 


def check(index, target):
  sequence.append(target)
  for i in range(1, (index//2) + 1):
    if sequence[-i:] == sequence[-2*i:-i]: 
      sequence.pop()
      return False
  sequence.pop()      
  return True

def dfs(current):
  if current == N:
    print("".join(sequence))
    exit()
  
  for i in range(3):
    if check(current+1, numbers[i]):
      sequence.append(numbers[i])
      dfs(current+1)
      sequence.pop()

N = int(input())
numbers = ["1", "2", "3"]
sequence = []
dfs(0)
