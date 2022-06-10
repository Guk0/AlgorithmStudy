# 문자열을 정해진 숫자만큼 잘라야함.
# 구역이 나눠진거라 생각하면 될듯. 맨 아래 예제 참고

def solution(s):
    len_s = len(s)
    result = len_s
    
    for i in range(1, len_s // 2 + 1) :
        target = s[:i]
        cnt = 0
        len_string = i
        for j in range(0, len_s, i):
            if target != s[j:j+i]:
                if cnt > 1:                                    
                    len_string += len(str(cnt))
                    
                if len(s[j:j+i]) == i:
                    target = s[j:j+i]
                    len_string += i
                    cnt = 1
                else:
                    len_string += len(s[j:j+i])
            else:
                if i + j >= len_s:
                    len_string += len(str(cnt))
                else:
                    cnt += 1
                
        result = min(result, len_string)
    
    return result