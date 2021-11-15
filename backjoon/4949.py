# while True:
#     num = list(input())
#     stack = list()
#     is_there = False

#     for i in range(len(num)):
#             if num[i] == '(' and '[':
#                 stack.append(num[i])
#             else:
#                 if not stack:
#                     is_empty = True
#                     break
#                 else:
#                     stack.pop()
while True:
    s = input()
    print(s)
    if s == '.':
        break
    stk = []
    temp = True
    for i in s:
        if i == '(' or i == '[':
            stk.append(i)
            print(stk)
        elif i == ')':
            if not stk or stk[-1] == '[':
                temp = False
                break
            elif stk[-1] == '(':
                stk.pop()
        elif i == ']':
            if not stk or stk[-1] == '(':
                temp = False
                break
            elif stk[-1] == '[':
                stk.pop()
    if temp == True and not stk:
        print('yes')
    else:
        print('no')