arr = [2,7,9,3,6,7,2,9,0,1]
s, e = map(int, input().split())
if s == 0:
    start = e+1
else:
    start = 0
for _ in range(2):
    for i in range(start+1, len(arr)):
        if i >= s and i<= e: continue
        arr[start], arr[i] = arr[i], arr[start]
print(*arr)