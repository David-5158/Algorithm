import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input()) # 노드의 개수

# 트리
Tree = [[] for _ in range(N+1)]    # 리스트 내포

# Tree = []
# for _ in range(N+1):
#     Tree.append([])

#부모 노드 저장
Parents = [0 for _ in range(N+1)]

# 트리 구조 입력
for _ in range(N-1) :
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)
    print(Tree)

def DFS(start, tree, parents) :
    # 연결된 노드들부터 parents[i]의 부모가 없으면 부모 설정 해주고, DFS 돌린다.
    for i in tree[start] :
        print(i)
        if parents[i] == 0 :
            print(i)
            parents[i] = start
            print(Parents)
            DFS(i, tree, parents)

DFS(1, Tree, Parents)

for i in range(2, N+1) :
    print(Parents[i])