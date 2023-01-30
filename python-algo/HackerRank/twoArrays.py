def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    if (any(a+b<k for a,b in zip(A,B))):
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        print(twoArrays(k, A, B))

        

