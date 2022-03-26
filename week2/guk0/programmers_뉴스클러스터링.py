# https://programmers.co.kr/learn/courses/30/lessons/17677
# 뉴스 클러스터링

import math
from collections import Counter

def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    # ord("A") ~ ord("Z") 65~90
    str1_arr = []
    str2_arr = []
    for i in range(len(str1)-1):
        if 65 <= ord(str1[i]) <= 90 and 65 <= ord(str1[i+1]) <= 90:
            str1_arr.append(str1[i] + str1[i+1])


    for i in range(len(str2)-1):
        if 65 <= ord(str2[i]) <= 90 and 65 <= ord(str2[i+1]) <= 90:
            str2_arr.append(str2[i] + str2[i+1])


    Counter1 = Counter(str1_arr)
    Counter2 = Counter(str2_arr)

    str_intersection = list((Counter1 & Counter2).elements())
    str_set = list((Counter1 | Counter2).elements())



    answer = math.floor((len(str_intersection) / len(str_set) * 65536)) if len(str_set) > 0 else 65536

    return answer