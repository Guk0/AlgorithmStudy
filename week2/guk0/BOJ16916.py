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
      j = table[j - 1]
        
    if char2[i] == char2[j]:
      j += 1
      table[i] = j

  return table


def kmp(char1, char2):
  table = make_table(char2)

  j = 0
  for i in range(len(char1)):
    while j > 0 and char1[i] != char2[j]:
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





# def check_is_sub(char1, char2):
#   char1, char2
#   index = 0
#   is_on_going = False
#   if len(char2) <= 1:
#     return 0

#   for i in range(len(char1)):
#     if char1[i] == char2[index]:
#       if is_on_going and index == len(char2)-1:
#         return 1
#       is_on_going = True
#       index += 1
      
#     else:
#       if is_on_going:
#         index = 0
#         is_on_going = False

#   return 0

# char1 = input()
# char2 = input()
# result = check_is_sub(char1, char2)
# print(result)