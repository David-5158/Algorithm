# n = 6
# edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

# node =[ [] for i in range(n+1)]

# print(node)

# for i in edge:
#     node[i[0]].append(i[1])
#     node[i[1]].append(i[0])
    
# print(node)

# for j in node[1]:
#     print(j)



# answer = 0
#-----------------------------------------------------------------

# from collections import deque, Counter

# def solution(n, edge):
#     answer = 0
#     graph = {}
#     for i in edge:
#         if i[0] in graph:
#             graph[i[0]].append(i[1])
#             print(graph)
#         else:
#             graph[i[0]] = [i[1]]
#             print(graph)
#         if i[1] in graph:
#             graph[i[1]].append(i[0])
#             print(graph)
#         else:
#             graph[i[1]] = [i[0]]
#             print(graph)
    
#     print(graph)
    
#     result = bfs(graph,1)
#     result = sorted(result.values(), reverse=True)
#     return list(Counter(result).values())[0]

# def bfs(edge,root):
#     visited = {}
#     queue=deque([[root,0]])
    
#     print ( queue )
#     arr = [[root,0]]
#     while queue:
#         current = queue.popleft()
#         print(current)
#         if current[0] not in visited:
#             visited[current[0]] = current[1]
#             print(visited)
#             add = set(edge[current[0]]) - set(visited)
#             queue += ([[i,current[1]+1] for i in add])
#     return visited

# print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]] ))

#------------------------------------------------------------------------------
from collections import deque
def solution(n, edge):
    graph = {}
    visited = [0]*n
    print(graph)
    for e in edge:
        graph[e[0]] = graph.get(e[0], []) + [e[1]]
        print(graph)
        graph[e[1]] = graph.get(e[1], []) + [e[0]]
        print(graph)
    queue = deque()
    queue.append(1)
    visited[0] = 1
    print(queue)
    while queue:
        nodes = len(queue)
        print(nodes)
        for i in range(nodes):
            current = queue.popleft()
            print("current=",current)
            for c in graph[current]:
                print("c =", c)
                if visited[c-1] == 0:
                    visited[c-1] = 1
                    print("visited =",visited)
                    queue.append(c)
                    print(queue)
    return nodes

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]] ))




# 딕셔너리 .get 사용법

# graph = {}
# graph[3] = graph.get(3, []) + [1,2,3]
# graph[5] = graph.get(5, []) + [4,5]
# print(graph)
# graph[3] = graph.get(3, []) + [4]
# graph[4] = graph.get(4, []) + [1]
# graph[4] = graph.get(4, []) + [5]
# print(graph)
# print(graph.values())