n = 5
lost = [2,4]
reserve = [1,3,5]
count = len(reserve)

for i in reserve:
    print(i)
    for j in lost:
        if j+1 or j-1 == i:
            print(i,j)
            count+=1
            print(count)
        
print(count)


