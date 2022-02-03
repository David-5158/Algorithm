from sys import stdin


def plusMinus(arr):
    plus,minus,zero = 0,0,0
    for i in arr:
        if i > 0:
            plus += 1
        elif i < 0:
            minus += 1
        else:
            zero += 1
    
    print(plus/len(arr))
    print(minus/len(arr))
    print(zero/len(arr))

if __name__ == "__main__":
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    
    plusMinus(arr)


# return print sep
# https://earthteacher.tistory.com/111


