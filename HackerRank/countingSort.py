from sys import stdin

def conuntingSort(arr):
    li = [0]*(max(arr)+1)
    # li = [0]*int(len(arr)-1)  이건 오류남 뭔차이지??
    
    for i in arr:
        li[i] += 1
    return li

num = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

print(*conuntingSort(arr))

# https://shareablecode.com/snippets/python-solution-for-hackerrank-problem-counting-sort-1-35nC-ttyq