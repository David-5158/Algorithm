import sys

def lonely_integer(a):
    res = 0
    for elem in a:
        res ^= elem # 비트 연산자 사용??? 이해 필요
    return res
    

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))

# https://singo112ok.tistory.com/34