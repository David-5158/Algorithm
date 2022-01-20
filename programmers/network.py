from collections import deque

def solution(n, computers):            
    
    def BFS(i):
        q = deque()
        q.append(i)
        
        print("q-->", q)
        while q:
            i = q.popleft()
            print("i-->",i)
            visited[i] = 1
            
            print("visited-->", visited)
            for a in range(n):
                if computers[i][a] and not visited[a]:
                    print("if",computers[i][a],"and not",visited[a])
                    q.append(a)
                    print(f"q.append({a})")
                
    answer = 0
    visited = [0 for i in range(len(computers))]
    
    for i in range(n):
        if not visited[i]:
            BFS(i)
            answer += 1
            print(answer)
        
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

