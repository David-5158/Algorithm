def solution(array, commands):
    answer = []
    for command in commands:
        pick = array[command[0]-1:command[1]]
        pick.sort()
        answer.append(pick[command[2]-1])
    return answer