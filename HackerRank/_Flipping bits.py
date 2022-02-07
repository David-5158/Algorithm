
def flippingBits(n):
    return 4294967295 -n

n = int(input())
for i in range(0,n):
    a = int(input())
    print(flippingBits(a))