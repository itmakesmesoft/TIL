arr = ['A','T','B','T','S']
N = int(input())
M = len(arr)
if N>0:
    for _ in range(N):
        for i in range(1, M):
            arr[i], arr[0] = arr[0], arr[i]
else:
    N = N*(-1)
    for _ in range(N):
        for i in range(1, M):
            arr[M-1], arr[M-i-1] = arr[M-i-1], arr[M-1]
print(arr)
    