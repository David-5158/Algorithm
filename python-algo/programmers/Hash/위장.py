def solution(clothes):
    # 1. 옷을 종류별로 구분하기
    hash_map = {}
    for clothe, type in clothes:
        print("type=", clothe, type)
        print("hash_map[type] = ",hash_map.get(type, 0) + 1)
        # type에 해당하는 값이 없으면 0으로 초기화 후 +1
        hash_map[type] = hash_map.get(type, 0) + 1
        
    # 2. 입지 않는 경우를 추가하여 모든 조합 계산하기
    answer = 1
    for type in hash_map: 
        print("hash_map=",hash_map)
        print("type=", type)
        print("hash_map[type]=",hash_map[type])
        answer *= (hash_map[type] + 1)
    
    # 3. 아무종류의 옷도 입지 않는 경우 제외하기
    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
