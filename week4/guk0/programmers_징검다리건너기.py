# https://programmers.co.kr/learn/courses/30/lessons/64062
# 징검다리 건너기
# 이분탐색

def check(stones, k, mid):    
    cnt = 0
    for stone in stones:        
        if stone - mid < 0:
            cnt += 1
        else:
            cnt = 0
        
        if cnt == k:
            return False

        
    return True
    
    
def solution(stones, k):
    start = min(stones)
    end = max(stones)

    answer = 0
    while start <= end:

        mid = (start + end) // 2;

        if check(stones, k, mid):            
            start = mid + 1;
            answer = max(answer, mid);
        else:
            end = mid - 1;
            
    return answer