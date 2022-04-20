# https://www.acmicpc.net/problem/4358
# 생태학
# 문자열 / 해시

from sys import stdin

input = stdin.readline
dic = {}

while True:
  text = input().strip()
  if not text:
    break

  if text in dic:
    dic[text] += 1
  else:
    dic[text] = 1

  
total = sum(dic.values())
for el in sorted(dic.keys()):
  # print(el, round(dic[el] * 100 / total, 4)) -> 틀림
  print("%s %.4f" %(el, dic[el] / total*100))