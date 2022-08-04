from collections import deque

def bfs(p):
    start = []
    
    for i in range(5): # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    
    print("start=",start)
    
    for s in start:
        queue = deque([s])  # 큐에 초기값
        print("queue=",queue)
        visited = [[0]*5 for i in range(5)]   # 방문 처리 리스트
        distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
        print("distance=",distance)
        visited[s[0]][s[1]] = 1
        print("visited=",visited)
        
        while queue:
            y, x = queue.popleft()
        
            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                        print("distance2  =", distance)
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    
    for i in places:
        answer.append(bfs(i))
    
    return answer
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))







# from collections import deque

# def bfs(p, idx):
#     q = deque([idx])
#     visited = [[False]*5 for _ in range(5)]
#     dic = {0: [0, -1], 1:[-1, 0], 2:[0, 1], 3:[1, 0]}
    
#     while q:
#         x, y, d = q.popleft()
#         visited[x][y] = True
        
#         for i in range(4):
#             nx = x + dic[i][0]
#             ny = y + dic[i][1]
#             nd = d + 1

#             if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
#                 visited[nx][ny] = True
                
#                 if p[nx][ny] == 'P':
#                     if nd <= 2:
#                         return False

#                 elif p[nx][ny] == 'O':
#                     if nd == 1:
#                         q.append([nx, ny, nd])

#     return True
                    
# def solution(places):
#     answer = []
    
#     for p in places:
#         flag = 1
        
#         for i in range(5):
#             for j in range(5):
#                 if p[i][j] == 'P':
#                     result = bfs(p, [i, j, 0])
#                     if not result:
#                         flag = 0
                        
#         answer.append(flag)
        
#     return answer