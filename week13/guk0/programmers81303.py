# https://programmers.co.kr/learn/courses/30/lessons/81303
# 표 편집
# pointer만 왔다갔다하면서 answer 값 변경 해주는 식으로 구현했는데.
# while문 돌때 시간초과가 나나봄.
# cmd 개수가 20만개니까 while 문 돌리면 안될 것 같음.

# linked_list로 풀면 된다. 간단하게 dict형태로 구현. 다음거 업데이트 해놓음.
# {0: [-1, 1], 1: [0, 2]}

def solution(n, k, cmd):
    answer = ["O" for _ in range(n)]
    linked_list = {i: [i-1, i+1] for i in range(n)}
    stack = []
    pointer = k
    for el in cmd: 
        cmd_arr = el.split(" ")
        if len(cmd_arr) > 1:
            command, number = cmd_arr            
            if command == "U":
                for i in range(int(number)):
                    pointer = linked_list[pointer][0]

            else:
                for i in range(int(number)):
                    pointer = linked_list[pointer][1]

        else:
            command = cmd_arr[0]
            if command == "C":
                answer[pointer] = "X"                
                pre, next = linked_list[pointer]
                stack.append(pointer)
                # -1인경우, n인경우
                if pre == -1:
                    linked_list[next][0] = pre
                    pointer = next
                elif next == n:
                    linked_list[pre][1] = next
                    pointer = pre
                else:
                    linked_list[pre][1] = next
                    linked_list[next][0] = pre
                    pointer = next
            else:
                index = stack.pop()
                pre, next = linked_list[index]
                answer[index] = "O"

                if pre == -1 :
                    linked_list[next][0] = index
                elif next == n :
                    linked_list[pre][1] = index
                else :
                    linked_list[pre][1] = index
                    linked_list[next][0] = index

                # if pointer >= index:
                #     pointer += 1
                
                
    return "".join(answer)
#     1: [0, 4]
#     # 2: [1, 4]
#     # 3: [2, 4]
#     4: [1, 5]