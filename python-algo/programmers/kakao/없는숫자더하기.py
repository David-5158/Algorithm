def solution(numbers):
    check = [num for num in range(10)]
    result = 0
    for i in numbers:
        check[i] = 0
    for j in check:
        if j != 0:
            result += j 
    return result
            
    

        
    

print(solution([1,6,4,3,8,9,0]))