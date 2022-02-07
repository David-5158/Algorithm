
def diagonalDifference(arr):
    left = 0
    right = 0
    
    for i in range(len(arr)):
        left = left + arr[i][i]
        right = right + arr[i][len(arr)-1-i]            
    return abs(left-right)

n= int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
print(diagonalDifference(arr))