import sys

n = sys.stdin.readline()
stack = []

for i in range(len(n)):
    stack.append(n[i])

for i in range(len(stack)):
    print(stack.pop(), end='')
    