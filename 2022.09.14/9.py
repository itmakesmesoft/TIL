arr = [
    [1,5,9],
    [7,0,3],
    [4,2,8]
]
n = int(input())
m = len(arr)
idx_list = list(map(int, input().split())) # 회전할 인덱스를 배열로 받음
for i in range(n):
    index = idx_list[i]
    for j in range(m):
        if index < m: # 행 회전
            arr[index][0], arr[index][j] = arr[index][j], arr[index][0]
        else:         # 열 회전
            arr[0][index-m], arr[j][index-m] = arr[j][index-m], arr[0][index-m]

for i in range(m): # 출력
    print(*arr[i])
