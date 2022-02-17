from collections import deque 
def solution(prices): 
    answer = [] 
    prices = deque(prices) 
    while(prices): 
        count = 0 
        now = prices.popleft() 
        for k in prices: 
            count+=1 
            if now>k: 
                break 
            answer.append(count) 
            
        return answer
print(solution([1,2,3,2,3]))