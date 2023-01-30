# import sys
# n = int(sys.stdin.readline())
# stackl = []
# stackr = []

# ps = sys.stdin.readline().split()
# print(ps)
# for i in range(n):
#     ps = sys.stdin.readline().split()
#     if ps == '(':
#         stackl.append('(')
#     if ps == ')':
#         stackr.append(')')
    
    # if len(stackl) == len(stackr):
    #     return print("YES")
    # else:
    #     return print("NO")

t = int(input())

for _ in range(t):
    ps = list(input())
    print(ps)
    stack = list()
    print(stack)
    is_empty = False
    for i in range(len(ps)):
        if ps[i] == '(':
            stack.append(ps[i])
        else:
            if not stack:
                is_empty = True
                break
            else:
                stack.pop()
    if not stack and not is_empty:
        print('YES')
    else:
        print('NO')


a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')