q = [0, 0]
truck_weights = [7, 4, 5, 6]
q.pop(0)
q.append(truck_weights.pop(0))
print(q)
print(truck_weights)
print(sum(q))
