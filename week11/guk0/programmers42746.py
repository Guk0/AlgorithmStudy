# https://programmers.co.kr/learn/courses/30/lessons/42746
# 가장 큰 수

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True) 
    # 각 원소는 3자리므로 *3을 하면 ex) 3, 30, 34 -> 333 303030, 343434.
    # 문자열로 했을 시 34, 3, 30 순
    # reverse가 먼저 적용되고 그다음에 key가 적용되는듯
    
    return str(int("".join(numbers))) # 0이 있으니까 int 변환 후 다시 str로 변환해야함.