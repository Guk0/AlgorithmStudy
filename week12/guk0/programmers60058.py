# https://programmers.co.kr/learn/courses/30/lessons/60058
# 괄호 변환

def is_balanced(arr):
    stack = []
    if not arr:
        return True
    
    for el in arr:
        if stack and el == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(el)
            
    return False if stack else True

def fix_signs(signs):
    # u, v로 나누되, u가 균형잡힌 문자열이어야 하므로 배열에 담아 개수 체크
    if is_balanced(signs):
        return signs
    
    sign_count = [0, 0] # sign_count가 일치할때 u,v로 쪼갬
    for i in range(len(signs)):
        if signs[i] == "(":
            sign_count[0] += 1
        else:
            sign_count[1] += 1

        if i > 0 and sign_count[0] == sign_count[1]:
            u = signs[:i+1]

            if is_balanced(u):
                return u + fix_signs(signs[i+1:])
            else:                
                for j in range(1, len(u)-1):
                    u[j] = ")" if u[j] == "(" else "("

                if len(u) > 2:
                    u = u[1:-1]
                else: 
                    u = []

                return ["(", *fix_signs(signs[i+1:]), ")"] + u
            

def solution(p):
    result = fix_signs(list(p))
    return "".join(result)

# 균형잡힌 문자열인지 판단할 수 있어야하고
# 완전한 문자열인지 판단할 수 있어야함.

       