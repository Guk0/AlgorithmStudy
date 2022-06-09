# https://programmers.co.kr/learn/courses/30/lessons/43238
# 입국심사
  
def solution(n, times):
    times.sort()
    len_times = len(times)
    
    left = 0
    right = max(times) * n
    answer = max(times) * n    
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        
        for i in range(len_times):
            cnt += mid // times[i]
            
        if cnt >= n:
            right = mid - 1
            answer = min(answer, mid)
        else:
            left = mid + 1
            
        
    return answer