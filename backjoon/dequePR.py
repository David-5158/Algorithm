from collections import deque

prices = [1,2,3,2,3]
queue = deque(prices)

print(queue)

answer = []

while queue:
    price = queue.popleft()
    time = 0
    for q in queue:
        time += 1
        if price > q:
            break
    answer.append(time)
return answer
