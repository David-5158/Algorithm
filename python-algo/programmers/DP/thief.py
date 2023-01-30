def solution(money): 
    answer = 0 
    dp1 = [0 for _ in range(len(money))] 
    dp2 = [0 for _ in range(len(money))] 
    dp1[0] = money[0] 
    dp1[1] = max(money[0], money[1]) 
    
    #마지막 집을 털지 않기때문W에 첫번째, 두번째 집 중 큰 집을 털면 된다. 
    dp2[0] = 0 
    #마지막 집을 터는 경우 첫번째 집을 털 수 없기 때문에 0으로 초기화. 
    dp2[1] = money[1] 
    for i in range(2, len(money)-1): 
    #마지막 집을 털지 않는 경우(첫번째 집을 털 수 있다.) 
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])
    
    for i in range(2, len(money)):
        #마지막 집을 터는 경우(첫번째 집을 털면 안된다.) 
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i]) 
    answer = max(max(dp1), max(dp2)) 
    return answer

print(solution([1,3,2,4,2,1]))