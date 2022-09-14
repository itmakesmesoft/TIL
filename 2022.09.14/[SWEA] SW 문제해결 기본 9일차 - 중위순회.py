def inorder(n):
    global N
    if n > N: return
    inorder(2*n)
    print(arr[n], end='')
    inorder(2*n+1)

for case in range(1, 11):
    N = int(input())
    arr = [0]*(N+1)
    for i in range(N):
        tmp = list(input().split())
        arr[int(tmp[0])]=tmp[1]
    print(arr)
    print(f'#{case}', end=' ')
    inorder(1)
    print()


'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S


'''