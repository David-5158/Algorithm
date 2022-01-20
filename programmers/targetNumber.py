def df(numbers, target):
    plus = [0]
    answer = 0
    for node in numbers:
        tmp = []
        for i in plus:
            tmp.append(i+node)
            tmp.append(i-node)
        plus = tmp
    for j in plus:
        if j == target:
            answer += 1
    return answer
        

print(df([1, 1, 1, 1, 1], 3))














#BFS 모든 방법 수
# def solution(numbers, target):
#     answer = 0
#     leaves = [0]
#     for num in numbers:
#         print(num)
#         tmp = []
#         print("tmp-->", tmp)
#         for parent in leaves:
#             print("parent-->", parent)
#             tmp.append(parent + num)
#             tmp.append(parent - num)
#             print("append tmp-->", tmp)
#         leaves = tmp
#         print("leaves-->", leaves)
#     for leaf in leaves:
#         print(leaves)
#         if leaf == target:
#             answer += 1
#     return answer

