def solution(n, computers):            
    
    def DFS(i):
        visited[i] = 1
        print(visited)
        for a in range(n):
            print("DFS for문")
            if computers[i][a] and not visited[a]:
                print("DFS if문")
                DFS(a)
                print("DFS 재귀문")
                
    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1
        
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))