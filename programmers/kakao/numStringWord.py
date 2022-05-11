def solution(s):
    enNum=['zero','one','two','three','four','five','six','seven','eight','nine']
    answer =''
    for idx,num in enumerate(enNum):
        if num in s:
            s=s.replace(num,str(idx))
        answer=s
    return int(answer)
print(solution("one4seveneight"))