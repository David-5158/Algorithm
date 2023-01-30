from itertools import combinations          # 중복허용(X), 순서의미(O) 인 조합을 import

def is_prime_number(num):
    if num==0 or num==1:
        return False
    else:
        for n in range(2, (num//2)+1):      # math를 사용하지 않고 (num//2)+1 까지로 설정
            if num%n == 0:
                return False
        
        return True

def solution(nums):
    answer = 0
    cmb = list(combinations(nums,3))        
    for arr in cmb:
        if is_prime_number(sum(arr)):     
            answer += 1                  
    
    return answer
