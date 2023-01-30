N,M,V=map(int,input().split())
matrix=[[0]*(N+1) for i in range(N+1)]  # 리스트 내포
print(matrix)
for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1
visit_list=[0]*(N+1)

def dfs(V):
    visit_list[V]=1 #방문한 점 1로 표시
    print(V, end=' ')
    for i in range(1,N+1):
        if(visit_list[i]==0 and matrix[V][i]==1):
            dfs(i)

def bfs(V):
    queue=[V] #들려야 할 정점 저장
    print(queue)
    print('!!')
    visit_list[V]=1 #방문한 점 1으로 표시
    print(visit_list)
    print('ㅇㅇ')
    
    while queue:
        V=queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            print(visit_list)
            if(visit_list[i]==0 and matrix[V][i]==1):
                queue.append(i)
                print(queue)
                print('??')
                visit_list[i]=1
                print(visit_list)
                print('//')

dfs(V)
visit_list=[0]*(N+1)
print()
bfs(V)





# from collections import deque
# import sys
# read = sys.stdin.readline

# def bfs(v):
#   q = deque()
#   q.append(v)       
#   visit_list[v] = 1   
#   while q:
#     v = q.popleft()
#     print(v, end = " ")
#     for i in range(1, n + 1):
#       if visit_list[i] == 0 and graph[v][i] == 1:
#         q.append(i)
#         visit_list[i] = 1

# def dfs(v):
#   visit_list2[v] = 1        
#   print(v, end = " ")
#   for i in range(1, n + 1):
#     if visit_list2[i] == 0 and graph[v][i] == 1:
#       dfs(i)

# n, m, v = map(int, read().split())

# graph = [[0] * (n + 1) for _ in range(n + 1)] 
# visit_list = [0] * (n + 1)
# visit_list2 = [0] * (n + 1)

# for _ in range(m):
#   a, b = map(int, read().split())
#   graph[a][b] = graph[b][a] = 1

# dfs(v)
# print()
# bfs(v)