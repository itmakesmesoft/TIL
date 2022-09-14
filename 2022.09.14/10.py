arr = [
    [1,3,5],
    [2,4,9],
    [7,2,0],
    [5,8,2]
]
n = int(input())

for i in range(4): # 슬라이싱 활용
    if n > 0:
        tmp = arr[i][3-n:]
        arr[i] = arr[i][:3-n]
        arr[i] = tmp + arr[i]
    else:
        tmp = arr[i][:n+1]
        arr[i] = arr[i][n:]
        arr[i] = arr[i] + tmp

for i in range(4): # 출력
    print(*arr[i])