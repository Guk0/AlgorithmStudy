# https://programmers.co.kr/learn/courses/30/lessons/64064
# 불량 사용자

def recursive(index, arr):
    global visited, answer, user_names, banned_names
    
    if index == len(banned_names):
        if set(arr) not in answer:
            answer.append(set(arr))
        return

    target = banned_names[index]    
    
    for i in range(len(user_names)):
        user = user_names[i]
        if len(user) == len(target) and not visited[i]:
            flag = True
            for j in range(len(user)):
                if target[j] == "*":
                    continue
                    
                if user[j] != target[j]:
                    flag = False
                    break
            
            if flag:
                visited[i] = True
                recursive(index + 1, arr+[user])
                visited[i] = False
            
            
def solution(user_id, banned_id):
    global answer, visited, user_names, banned_names
    user_names = user_id
    banned_names = banned_id
    answer = []
    visited = [False for _ in range(len(user_names))]
    recursive(0, [])
    return len(answer)