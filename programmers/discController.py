import heapq 

def solution(jobs): 
    answer = 0 
    end, i = 0, 0 
    start = -1 
    hq = [] 
    while len(jobs)>i:
        print("start-->",start, end)
        for job in jobs:
            print(job)
            if start<job[0]<=end:
                heapq.heappush(hq, (job[1], job[0]))
                print(hq)
        
        if len(hq)>0: 
            now = heapq.heappop(hq) 
            start = end 
            end += now[0] 
            answer += (end-now[1]) 
            i += 1 
        else: 
            end+=1 
    answer = answer//len(jobs) 
    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))