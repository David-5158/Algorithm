def bfs(begin, target, words, visited):
    count = 0
    stack = [(begin, 0)]
    print(type(stack[0]))
    while stack:
        print(stack)
        cur, depth = stack.pop()
        if cur == target:
            return depth
        
        print("start for 문")
        for i in range(len(words)):
            if visited[i] == True:
                print("if문")
                continue
            cnt = 0
            print("cnt:",cnt)
            for a,b in zip(cur, words[i]):
                print("zip (a,b): ",a,b)
                if a!=b:
                    cnt += 1
            if cnt == 1:
                visited[i] = True
                stack.append((words[i], depth+1))
                print("Stack.append:",stack)
                
            

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    visited = [False]*(len(words))
    print(visited)

    answer = bfs(begin, target, words, visited)

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))