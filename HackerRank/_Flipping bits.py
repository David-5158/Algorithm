
# 4294967295 = 32비트 부호 없는 정수 의 최대값
# 4294967295 - n = XOR과 같은 역할
# 부호 반대 
def flippingBits(n):
    return 4294967295 -n

n = int(input())
for i in range(0,n):
    a = int(input())
    print(flippingBits(a))