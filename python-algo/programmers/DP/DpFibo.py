fiboData = [0 for i in range(100)]
fiboData[0] = 0
fiboData[1] = 1

def fibo(n):
  if (n<=2):
    return 1
  if (fiboData[n]==0):
    fiboData[n] = fibo(n-1) + fibo(n-2)
  return fiboData[n]

print(fibo(6))    