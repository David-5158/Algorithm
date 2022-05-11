from collections import deque
def solution(record):
    answer = []
    dic = {}
    # 아이디 히스토리 변경 저장
    for i in record:
        result = i.split()
        if len(result) == 3:
            dic[result[1]] = result[2]
        else:
            continue
    
    for j in record:
        result = j.split()
        if result[0] == 'Enter':
            answer.append(dic[result[1]]+"님이 들어왔습니다.")
        elif result[0] == 'Leave':
            answer.append(dic[result[1]]+"님이 나갔습니다.")
        else:
            continue
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))