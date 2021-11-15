import sys
from typing import Deque
n = int(sys.stdin.readline())
queue = Deque([])

for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
