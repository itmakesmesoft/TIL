arr = ['T','B','T','S','A','K','L','I','Z','C']
a, b = map(int, input().split())
for _ in range(2):
    for i in range(a+1, b+1):
        arr[i], arr[a] = arr[a], arr[i]
print(*arr)