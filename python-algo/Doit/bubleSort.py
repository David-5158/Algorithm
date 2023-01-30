def bublesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [9,1,3,4,6,7,8]
bublesort(arr)

for i in range(len(arr)):
    print(f'{arr[i]}', end='')