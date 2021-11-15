input_num = int(input())
numbers = list(map(int, input().split())) 

numbers.sort() 
input_num2 = int(input()) 
numbers2 = list(map(int, input().split())) 
for num in numbers2: 
    left, right = 0, len(numbers) - 1 
    is_find = False 
    
    while True: 
        median = (left + right) // 2 
        if num == numbers[median]: 
            print(1) 
            is_find = True 
            break 
        elif num > numbers[median]: 
            left = median + 1 
        elif num < numbers[median]: 
            right = median - 1 
        if left > right: 
            break 
        
    if not is_find: 
        print(0)



# N1 = int(input())
# num = list(map(int, input().split()))
# num.sort()
# N2 = int(input())
# num2 = list(map(int, input().split()))

# for number in num2:
#     left, right = 0, len(num)-1
#     correct = False

#     while True:
#         mid = (left + right)//2
#         if number == num[mid]:
#             print(1)
#             right = True
#             break
#         elif number > num[mid]:
#             left = mid + 1
#         elif number < num[mid]:
#             right = mid - 1
        
#         if left > right:
#             break

#     if not correct:
#         print(0)

