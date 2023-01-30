from sys import stdin

num = list(map(str, stdin.readline().split()))

count = 0

print('abcde'.startswith('abc'))

if num[0] == 'love':
    count = count + 1
else:
    print("찾지못했습니다")

print(count)