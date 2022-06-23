# https://programmers.co.kr/learn/courses/30/lessons/12911
# 다음 큰 숫자

def to_binary(number):
    cnt = 0
    while number > 0:
        if number % 2 == 1:
            cnt += 1
        number = number // 2

    
    return cnt

def solution(n):
    cnt = to_binary(n)

    n += 1
    while cnt != to_binary(n):
        n += 1

    return n


# 1010101
# 1010110

# 1001110
# 1010011

# 1111
# 10111

# 2 4  8   16   32     64     
# 1 11 111 1111 11111 111111 1111110


# 5 100
# 6 101
# 7 110
# 8 111