# https://programmers.co.kr/learn/courses/30/lessons/87377
# 교점에 별 만들기

def solution(line):
    answer = []

    # 2x - y + 4 = 0
    # -2x - y + 4 = 0
    # -y + 1 = 0
    # 5x - 8y - 12 = 0
    # 5x + 8y + 12 = 0

    arr = []
    dict = {}
    for i in range(len(line)):
        for j in range(i, len(line)):
            A, B, E = line[i] 
            C, D, F = line[j]

            if A*D - B*C != 0:
                x = (B*F - E*D) / (A*D - B*C)
                y = (E*C - A*F) / (A*D - B*C)

                if x.is_integer() and y.is_integer() and [int(x), int(y)] not in arr:
                    arr.append([int(x), int(y)])

    arr.sort(key=lambda x: (x[1], x[0]))

    for i in range(arr[0][1], arr[-1][1]+1):
        dict[i] = []
        for el in arr:
            if i == el[1]:
                dict[i].append(el[0])

    range_arr = [int(1e9), int(-1e9)]
    for key in dict:
        if len(dict[key]) > 1:            
            range_arr[0] = min(range_arr[0], abs(dict[key][0]))
            range_arr[1] = max(range_arr[1], abs(dict[key][-1]))
           


    for key in dict:
        char = ""
        if len(dict[key]) > 0:
            for i in range(range_arr[0], range_arr[1]+1):
                if i in dict[key]:
                    char += "*"
                else:
                    char += "."
        else:
            char = "." * (abs(range_arr[1] - range_arr[0]) +1)
        
        answer.append(char)

    return answer