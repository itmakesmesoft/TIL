def isSame(index): # True/False
    for i in range(m):
        if arr[i+index] != put[i]: return False
    return True

arr = ['S','E','Y','U','I','O','Q','X','D','E']
put = input() # YUIOQ
n = len(arr)
m = len(put)
for i in range(n-m):
    if isSame(i):
        start, end = i, i+m
        break

for _ in range(2): # 회전
    for i in range(start+1, end):
        arr[start], arr[i] = arr[i], arr[start]
print(*arr)