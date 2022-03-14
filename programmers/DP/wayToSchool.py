def solution(m, n, puddles):
    answer = 0
    graph = [[0]*(m+1) for i in range(n+1)]
    print(graph)
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1: #(1,1)은 1으로 초기화
                graph[1][1]=1
            elif [j,i] not in puddles: # 물웅덩이가 아닌경우
                graph[i][j] = graph[i-1][j]+graph[i][j-1]
                print(graph[i][j])
    
    for i in range(4):
        print(graph[i])
                
    return graph[n][m]%1000000007

print(solution(4,3,[[2,2]]))