def solution(name):
    name = list(name)
    answer = 0
    i = 0
    
    while True:
        answer += min(ord(name[i])-ord('A'), ord('Z')-ord(name[i])+1)
        name[i] = 'A'
        
        if name.count('A') == len(name) : return answer
        
        left, right = 1,1
        for l in range(1,len(name)):
            if name[i-l] == 'A': 
                left += 1 
                print('l')
            else: break
        
        for r in range(1,len(name)):
            if name[i+r] == 'A': 
                right += 1
                print('r')
            else: break
        if left < right:
            answer += left
            i -= left   # 위치 세팅 [ -1:,,,]
        else:
            answer += right
            i += right
            
            
    return answer


# from collections import deque
# from itertools import product

# def solution(name):    
#     results = []

#     for rs in product((-1,1), repeat=len(name)-1):
#         name_deque = deque(name)
#         default = deque('A'*len(name))

#         for c, r in enumerate([0]+list(rs)):
#             default.rotate(r)
#             name_deque.rotate(r)
#             default[0] = name_deque[0]

#             if name_deque == default:
#                 results.append(c)
#                 break

#     return min(set(results))+sum([min(ord(l)-ord('A'), ord('Z')-ord(l)+1) for l in name])

from itertools import product


name = "JEROEN"


print(list(product((-1,1), repeat=len(name)-1)))
