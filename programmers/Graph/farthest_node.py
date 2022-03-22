n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

node =[ [] for i in range(n+1)]

print(node)

for i in edge:
    node[i[0]].append(i[1])
    node[i[1]].append(i[0])
    
print(node)

for j in node[1]:
    print(j)
    

answer = 0
