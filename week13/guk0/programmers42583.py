# https://programmers.co.kr/learn/courses/30/lessons/42583
# 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0]*bridge_length)
    current_weight = 0
    
    while queue:
        current_weight -= queue.popleft()
        answer += 1
               
        if truck_weights:
            if current_weight + truck_weights[0] <= weight and len(queue) < bridge_length:
                truck = truck_weights.pop(0)
                queue.append(truck)
                current_weight += truck
            else:
                queue.append(0)

    return answer