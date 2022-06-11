# https://programmers.co.kr/learn/courses/30/lessons/12899
# 124 나라의 숫자

def solution(n):
    answer = ''
    numbers = [4, 1, 2]
    arr = [n]
    while n > 3:
        if n % 3 == 0:        
            n = (n - 3) // 3
        elif n % 3 == 2:
            n = (n - 2) // 3
        else:
            n = (n - 1) // 3
        arr.append(n)
    
    arr.sort()

    for el in arr:
        answer += str(numbers[el%3])
        
    
    return answer



#   1 2 4
# # 1 2 3 
#   11 12 14 21 22 24 41 42 44
# #  4  5  6  7  8  9 10 11 12  
#   111 112 114 121 122 124 141 142 144
# #  13  14  15  16  17  18  19  20  21
#   211 212 214 221 222 224
# #  22  23  24  25  26  27

# N이 3으로 나눠 떨어지면 N-3
# N을 3으로 나눴을때 나머지가 2이면 N-2
# N을 3으로 나눴을때 나머지가 1이면 N-1
# N-1 // 3

# 위 조건에 맞게 list를 구성하고 정렬한 뒤 
# for 문 돌려 다시 변환함.