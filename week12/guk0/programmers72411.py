# https://programmers.co.kr/learn/courses/30/lessons/72411
# 메뉴 리뉴얼

from itertools import combinations


def solution(orders, course):
    answer = []    
    
    for number in course:
        order_dict = {}
        for order in orders:
            sorted_order = sorted(list(order))
            combis = combinations(sorted_order, number)
            for el in combis:
                el = "".join(el)
                if el in order_dict:
                    order_dict[el] += 1
                else:
                    order_dict[el] = 1
        
        if order_dict:
            max_value = max(order_dict.values())
            if max_value >= 2:
                for key in order_dict:
                    if order_dict[key] == max_value:
                        answer.append(key)
                
    answer.sort()
    return answer