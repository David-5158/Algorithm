import sys

N = int(sys.stdin.readline())
queue = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(queue)==0:
            print(0)
        else:
            queue.sort(reverse=True)
            print(queue.pop(0))
    else:
        queue.append(num)
    

