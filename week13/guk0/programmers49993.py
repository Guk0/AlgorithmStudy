# https://programmers.co.kr/learn/courses/30/lessons/49993
# 스킬트리

def solution(skill_order, skill_trees):
    answer = 0
    order_len = len(skill_order)
    order_set = set(skill_order)
    
    for skill_tree in skill_trees:
        index = 0
        flag = True
        for skill in skill_tree:
            if skill in order_set:
                if skill == skill_order[index]:
                    index += 1
                else:
                    flag = False
                    break
        
        if flag:
            answer += 1
            
    
    return answer