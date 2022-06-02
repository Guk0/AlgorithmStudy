# https://www.acmicpc.net/problem/16916
# 부분 문자열
# 문자열 / KMP 알고리즘

# ababad
# abad
# 라는 문자열이 들어올 때 abab까지 확인 후 다르다고 판명 나면 ab 다음부터 다시 시작해야함.
# 이러한 처리를 안해주면 부분 문자열이 없게 나옴.



def make_table(char2):  
  table = [0] * len(char2)
  j = 0

  for i in range(1, len(char2)):
    while j > 0 and char2[i] != char2[j]:
      # 같은거 만날때까지 계속 j-1 빼야함.
      # 0 혹은 같은거 만나면 종료
      # 초기에는 index 0번과 j가 일치해야 늘어남
      j = table[j - 1]
        
    if char2[i] == char2[j]:
      # 일단 +1 하고 다음 루프에서 문자열 같다면 j+1 그대로 사용 아니면 다시 j-1 씩하여 같을때까지 찾음
      j += 1      
      table[i] = j

  return table


def kmp(char1, char2):
  table = make_table(char2)  

  j = 0
  for i in range(len(char1)):
    while j > 0 and char1[i] != char2[j]:
      # char1[i]와 같은 문자가 나올때까지 j-1 혹은 0으로 초기화
      j = table[j - 1]

    if char1[i] == char2[j]:
      if j == len(char2) - 1:
        return 1
      else:
        j += 1

  return 0


char1 = input()
char2 = input()
print(kmp(char1, char2))

# [0, 0, 1, 2, 3, 4, 5, 6, 0]
# table[j-1]번 인덱스와 j-1번 인덱스가 같다면 거기부터 시작할 수 있음
# 33번째 -> j = talbe[j-1]
# ABABABABBABABABABC
# ABABABABC



# ABABBABABC
# ABABC

