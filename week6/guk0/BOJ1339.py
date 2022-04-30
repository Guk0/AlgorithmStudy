# https://www.acmicpc.net/problem/1339
# 단어 수학
# 그리디

# 3
# ABCDEF
# FGD
# GFC
# {'A': 100000, 'B': 10000, 'C': 1001, 'D': 101, 'E': 10, 'F': 111, 'G': 110}
# 다음과 같이 dict로 저장해두고 value만 sort(reverse)하여 큰값부터 차례대로 987..1 곱해줌

from sys import stdin

input = stdin.readline

N = int(input())
arr = [input().strip() for _ in range(N)]
alpha_dict = {}


for alpha in arr:
    for j in range(len(alpha)):
        if alpha[j] in alpha_dict:
            alpha_dict[alpha[j]] += 10 ** (len(alpha)-j-1)
        else:  
            alpha_dict[alpha[j]] = 10 ** (len(alpha)-j-1)

nums = [val for val in alpha_dict.values()]
nums.sort(reverse=True)

answer = 0
cnt = 9
for num in nums:
  answer += num * cnt
  cnt -= 1

print(answer)



# 부르트포스로 풀다가 막힘.

# from sys import stdin

# input = stdin.readline

# N = int(input())
# arr = [i for i in range(10)]
# texts = [input().strip() for _ in range(N)]
# texts.sort(key=lambda x: len(x), reverse=True)
# alphabet_dict = {chr(i): None for i in range(ord("A"), ord("Z")+1)}
# numbers = [[] for _ in range(N)]
# text_len_dict = {}

# for text in texts:
#   try:
#     text_len_dict[len(text)].append(text)
#   except:
#     text_len_dict[len(text)] = [text]

# first_text = texts[0]
# for i in range(len(first_text)):  
#   if alphabet_dict[first_text[i]] != None:
#     numbers[0] = int(str(numbers[0]) + str(alphabet_dict[first_text[i]]))
#   else:
#     if len(text_len_dict[i]) > 1:
#       tmp = []
#       for el in text_len_dict[i]:
#         for i in range(len(el)):

#     else:
#       num = arr.pop()
#       alphabet_dict[first_text[i]] = num
#       numbers[0] = int((str(numbers[0]) if numbers[0] else "") + str(num))


# print(numbers)
# ABCDEF
# 987436 987435 앞에꺼가 더 큼.
# FGD
# 654 564
# GFC
# 567 657

# GF
# EG
