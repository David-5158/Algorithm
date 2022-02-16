def fibo(n):
    if (n<=2):
      return 1
    else:
      return fibo(n-1) + fibo(n-2)
  
print(fibo(6))

# fibo(4)의 연산이 두 번, fibo(3)의 연산이 
# 세 번 진행되는 것을 볼 수 있습니다. 
# 이미 진행됐던 연산인데도 불구하고
# -> 해결하기위해 DP 등장!!!