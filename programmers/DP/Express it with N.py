def solution(N, number):
    
    if number == N:
        return 1
    
    answer = -1
    # 큰 문제 -> 여러개의 작은 문제들로 쪼개어 접근
    _li = [set() for i in range(8)]
    # li = [set()] * 8 인덱스가 모두 같은 주소를 가지고 있기때문에 하나를 바꾸면 모두 바뀌게된다 주의
    
    print(_li)
    # _li
    # set() set()                   set() set() set() set() set() set()
    # 5     55, 5-5, 5+5, 5*5, 5//5 
    # 5를 하나 썻을때 , 두개 썻을 때,,,세개,,각각의 값들을 set에 넣어준다.
    
    # 1 2  3   4    5     6      7      8 
    # 5 55 555 5555 55555 555555 555555 55555555
    
    for i in range(len(_li)):
        _li[i].add(int(str(N)*(i+1)))
    print(_li)
    for i in range(1,8):
        for j in range(i):
            for op1 in _li[j]:
                for op2 in _li[i-j-1]:
                    _li[i].add(op1+op2)
                    _li[i].add(op1-op2)
                    _li[i].add(op1*op2)
                    if op2 != 0:
                        _li[i].add(op1//op2)
                        
        if number in _li[i]:
            answer = i+1
            break
                    
    return answer