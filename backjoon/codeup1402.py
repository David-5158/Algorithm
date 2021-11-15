n = int(input())
stack = []
for i in range(n):
    num = list(map(int, input().split()))
    for i in range(len(num)):
        stack.pop(num[i])
    
    print(stack)
