print('세 정수중 최대값은?')

a = int(input('정수 a: '))
b = int(input('정수 b: '))
c = int(input('정수 c: '))

max = a

if b > max: max=b
if c > max: max=c

print(max)