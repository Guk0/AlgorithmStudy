# https://programmers.co.kr/learn/courses/30/lessons/42839
# 소수찾기

import itertools
import math

def check(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True



def solution(numbers):

    answer = 0
    arr = []
    for i in range(len(numbers)):
        target = []
        if i == 0:
            target = list(numbers)
        else:
            permutation = itertools.permutations(list(numbers), i+1)
            perm = set(permutation)
            target = list(map(list, perm))


        for el in target:
            int_el = int("".join(el))
            if int_el == 1 or int_el == 0:
                continue
            
            if len(str(int_el)) == i+1 and check(int_el) and int_el not in arr:
                arr.append(int_el)
                answer += 1


    return answer