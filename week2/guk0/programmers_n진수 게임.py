# https://programmers.co.kr/learn/courses/30/lessons/17687?language=python3
# n진수 게임

import string

def solution(n, t, m, p):

    tmp = string.digits+string.ascii_uppercase
    def convert(num, base) :
        q, r = divmod(num, base)
        if q == 0 :
            return tmp[r] 
        else :
            return convert(q, base) + tmp[r]


    arr = []
    current = 0
    index = 1
    while len(arr) < t:
        parsed_number = convert(current, n)
        for el in list(parsed_number):
            if len(arr) >= t:
                break
            if index == p:
                arr.append(el)

            if index == m:
                index = 1
            else:
                index += 1

        current += 1

    return "".join(arr)