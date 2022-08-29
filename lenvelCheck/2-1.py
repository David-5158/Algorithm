def solution(n, words):
    answer = [0,0]
    stack = [words[0]]
    for i in range(1, len(words)):
        if stack[-1][-1] == words[i][0] and words[i] not in stack:
            stack.append(words[i])
            
            print(stack)
        else:
            answer[0] = (i % n) + 1
            answer[1] = i // n + 1
            break
    return answer


# print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
# print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))


# [3,3]
# [0,0]
# [1,3]