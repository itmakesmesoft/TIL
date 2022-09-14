arr = [3, -1, 1, -1, 2, -1, 8, -1, 9]
N = int(input())
for _ in range(N):
    for i in range(1, len(arr)):
        if arr[i]==-1: continue
        arr[0], arr[i] = arr[i], arr[0]
        
for i in range(len(arr)):
    print('#', end=' ') if arr[i]==-1 else print(arr[i], end=' ')

    