def solution(triangle):
    for i in range(1, len(triangle)):
        print(len(triangle))
        for j in range(i+1):
            if j == 0:    
                triangle[i][j] += triangle[i-1][j]  # 왼쪽 테두리 더해주기
            elif j == i: 
                triangle[i][j] += triangle[i-1][j-1]  # 오른쪽 테두리 더해주기
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])  # 나머지 연산
                
    return max(triangle[-1]) # 배열 마지막 [4, 5, 2, 6, 5]중 max 값 찾은 후 리턴

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

# https://codedrive.tistory.com/49