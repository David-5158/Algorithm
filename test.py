# def solution(n, words):
#     answer = []
#     check = []
#     number = [ [] for i in range(n)]
#     for i in range(len(words)-1):
#         if words[i][-1] != words[i+1][0]:
#            answer.append(i%n)
#     for j, word in enumerate(words):
#         number[j%n].append(word)
#         if word in check:
#             answer.append((j+1)//n)
#         else:
#             check.append(word)
#             print(check)

#     return answer

arr = ["abc","texd"]
word = "text"

if word[0] == arr[-1][-1]:
    print("true")
else:
    print("fuck")