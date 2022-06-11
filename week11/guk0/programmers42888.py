# https://programmers.co.kr/learn/courses/30/lessons/42888
# 오픈 채팅방

def solution(record):
    answer = []
    id_dict = {}
    name_dict = {}
    
    for el in record:
        operator, *user = el.split(" ")
        if operator == "Enter":
            uid, name = user
            if uid in name_dict and name_dict[uid] != name:
                for i in id_dict[uid]:                
                    answer[i] = name + "님" + answer[i].split("님")[1]
                    
            name_dict[uid] = name
            answer.append(name +"님이 들어왔습니다.")
            
            if uid in id_dict:
                id_dict[uid].append(len(answer)-1)
            else:
                id_dict[uid] = [len(answer)-1]
        elif operator == "Leave":
            uid = user[0]
            name = name_dict[uid]
            answer.append(name+"님이 나갔습니다.")
            id_dict[uid].append(len(answer)-1)
        else:
            uid, name = user
            name_dict[uid] = name
            for i in id_dict[uid]:                
                answer[i] = name + "님" + answer[i].split("님")[1]
            
    return answer