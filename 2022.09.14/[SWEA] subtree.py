t = int(input())
for case in range(1, t+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    left_child = [0]*(E+2)
    right_child = [0]*(E+2)

    for i in range(E):
        index, val = arr[2*i], arr[2*i+1]
        if left_child[index]==0:
            left_child[index] = val
        else:
            right_child[index] = val

    def search(now):
        global cnt
        if now: 
            cnt += 1
            search(left_child[now])
            search(right_child[now])

    cnt = 0
    search(N)
    print(f'#{case} {cnt}')


'''
test case
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''