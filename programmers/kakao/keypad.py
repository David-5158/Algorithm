def solution(numbers, hand):
    answer = ''
    key = {1:[0,0], 2:[0,1], 3:[0,2], 
           4:[1,0], 5:[1,1], 6:[1,2], 
           7:[2,0], 8:[2,1], 9:[2,2], 
         '*':[3,0], 0:[3,1],'#':[3,2]}
    
    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key[i]
            lPos = key[lhand]
            rPos = key[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])
            
            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))



# def solution(numbers, hand):
#     answer = ''
#     key = {1:[2,4], 2:[1,3,4], 3:[2,6], 
#            4:[1,5,7], 5:[2,4,6,8], 6:[3,5,9], 
#            7:[4,8,10], 8:[5,7,9,0], 9:[6,8,12], 
#            10:[7,0], 0:[8,10,12],12:[0,9]}
#     current = {"L": 10, "R": 12 }
        
#     for num in numbers:
#         if num in [1,4,7]:
#             answer +=  "L"
#             current["L"] = num
#         elif num in [3,6,9]:
#             answer += "R"
#             current["R"] = num
#         else:
#             if current["L"] == num:
#                 answer += "L"
#             elif current["R"] == num:
#                 answer += "R"
#             else:
                
    
    
#     return answer

# def network(current, num, key):
#     count = []
#     current = current
#     for i in key[num]:
#         if num in key[i]:
#             count.append(2)
        
        
            
        
        
#     key[L] = 
    
# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))