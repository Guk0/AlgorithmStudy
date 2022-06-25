# https://programmers.co.kr/learn/courses/30/lessons/17684
# [3차] 압축


def solution(msg):
    alpha_dict = {chr(i+64): i for i in range(1, 27)}
    visited = [False for _ in range(len(msg))]
    last_index = 26
    answer = []
    
    i = 0
    while i < len(msg):
        current = msg[i]
        while True:
            if current in alpha_dict:
                i += 1
                if i < len(msg):
                    current += msg[i]
                else:
                    answer.append(alpha_dict[current])
                    break
            else:
                last_index += 1
                alpha_dict[current] = last_index
                answer.append(alpha_dict[current[:-1]])
                break
        
    return answer