# https://programmers.co.kr/learn/courses/30/lessons/81302
# 거리두기 확인하기

# O일때만 stack에 append한다. X이면 확인할 필요 없고 P이면 무조건 return 0.

def solution(places):
    answer = []
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]        
    
    def dfs(coordinate):
        stack = []
        visited = [[False for _ in range(5)] for _ in range(5)]
        y, x = coordinate[0], coordinate[1]
        stack.append([y, x])
        visited[y][x] = True
        while stack:
            tmp_y, tmp_x = stack.pop()

            for i in range(4):
                ny = tmp_y + dy[i]
                nx = tmp_x + dx[i]
                if abs(y - ny) + abs(x - nx) <= 2 and 0 <= ny <= 4 and 0 <= nx <= 4 and not visited[ny][nx]:
                    if graph[ny][nx] == "P":
                        return 0
                    
                    if graph[ny][nx] == "O":
                        visited[ny][nx] = True
                        stack.append([ny, nx])
                    
        return 1
    
    for place in places:
        graph = []
        P_list = []
        result = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    P_list.append([i, j])

            graph.append(list(place[i]))
        
        for P in P_list:
            if dfs(P) == 0:
                result = False
                break
            
            
        answer.append(1 if result else 0)
    
    return(answer)
    

        
    
    