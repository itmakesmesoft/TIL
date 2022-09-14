arr = [6,9,2,0,4,6,7,1,9,3]
s1, e1, s2, e2 = map(int, input().split())
for _ in range(2):
    for i in range(len(arr)):
        if i > s1 and i <= e1:
            arr[s1], arr[i] = arr[i], arr[s1]
        elif i > s2 and i <= e2:
            arr[s2], arr[i] = arr[i], arr[s2]
print(*arr)