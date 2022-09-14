arr = [9, 3, 5, 7, 4]
N = int(input())
for _ in range(N):
    for i in range(1, len(arr)):
        arr[0], arr[i] = arr[i], arr[0] 
print(*arr)