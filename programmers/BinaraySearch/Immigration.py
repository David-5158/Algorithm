def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    
    while (left <= right):
        print('left, right =', left,right)
        mid = (left + right) //2
        print('mid =',mid)
        people =0
        for time in times:
            people += (mid // time)
            print('people =',people)
            if people >= n:
                break
        print('Pluspeople =',people)   
        if people >= n:
            answer = mid
            right = mid -1
            
        elif people < n:
            left = mid +1
            
    return answer

print(solution(6,[7,10]))