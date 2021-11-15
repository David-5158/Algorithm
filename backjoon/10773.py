import sys
n = int(sys.stdin.readline())
stack = []
result = 0

for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

for i in range(len(stack)):
    result += stack[i]

print(result)