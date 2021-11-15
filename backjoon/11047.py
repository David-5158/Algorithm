n, k = map(int, input().split())
m = []
num = 0
for i in range(n):
    m.append(int(input()))
for i in range(n - 1, -1, -1):
    if k == 0:
        break
    if m[i] > k:
        print(m[i],k)
        continue
    num += k // m[i]
    print(num)
    k %= m[i]
    print(k)
print(num)

# N, K = map(int, input().split()) 
# coin_lst = list()
# for i in range(N):
#     coin_lst.append(int(input()))

# count = 0
# for i in reversed(range(N)):
#     count += K//coin_lst[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
#     K = K%coin_lst[i] # K는 동전으로 나눈 나머지로 계속 반복

# print(count)
