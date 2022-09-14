arr = [3,4,1,1,2]
index = int(input())
for i in range(1, len(arr)):
    arr[0], arr[i] = arr[i], arr[0] 
print(*arr)