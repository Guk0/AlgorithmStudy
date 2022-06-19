# https://programmers.co.kr/learn/courses/30/lessons/67257
# 수식 최대화

from itertools import permutations

def solution(expression):
    answer = []
    expression_arr = []
    operators = ["*", "+", "-"]
    
    string = ""
    for el in expression:
        if el in operators:
            expression_arr.append(string)
            expression_arr.append(el)
            string = ""            
        else:
            string += el
    expression_arr.append(string)
    
    # 연산을 stack으로 처리 가능
    for operation_order in permutations(operators, 3):
        arr = expression_arr[:]
        for operator in operation_order:
            i = 0
            while i < len(arr):
                if arr[i] == operator:
                    if operator == "*":
                        arr[i] = int(arr[i-1]) * int(arr[i+1])
                    elif operator == "+":
                        arr[i] = int(arr[i-1]) + int(arr[i+1])
                    else:
                        arr[i] = int(arr[i-1]) - int(arr[i+1])
                    del arr[i-1]
                    del arr[i]
                else:
                    i += 1

        answer.append(abs(arr[0]))
    
            
    
    return max(answer)