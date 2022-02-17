from collections import deque

scoville = [1,2,3,9,10,12]
K = 7

queue = deque(scoville)
check = []

cnt = 0
while queue:
    if queue[0] < K:
        if queue[0] > queue[1]:
            mix = queue[1]+(queue[0]*2)
            cnt+=1
            del queue[0]
            del queue[0]
            print("befor del", queue)
            queue.insert(0,mix)
            print("q[0] > q[1]",queue)
        else:
            mix = queue[0]+(queue[1]*2)
            cnt+=1
            del queue[0]
            del queue[0]
            print("befor del", queue)
            queue.insert(0,mix)
            print("q[0] < q[1]",queue)
    else:
        check.append(queue.popleft())
        
print(cnt)