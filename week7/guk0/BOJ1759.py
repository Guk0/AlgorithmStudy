# https://www.acmicpc.net/problem/1759
# 암호 만들기
# 백트래킹

# 알파벳은 증가하는 순서(abc 가능. bac 불가)


def dfs(password, index):
  if len(password) == L:
    cnt = 0
    for char in password:
      if char in vowels:
        cnt += 1

    if cnt >= 1 and L - cnt >= 2:
      answer.append(password)
    return

  for i in range(index+1, C):
    dfs(password + arr[i], i) 

  

L, C = map(int, input().split())
arr = input().split()
arr.sort()
vowels = ["a", "e", "i", "o", "u"]
answer = []


for i in range(C):
  dfs(arr[i], i)

answer.sort()
print("\n".join(answer))