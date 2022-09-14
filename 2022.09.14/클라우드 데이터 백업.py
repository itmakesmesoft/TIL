N=int(input())
data = [input() for _ in range(N)]

y = 0 # 초기값 0 (값은 무의미)
for i in range(2): # i=0 행 탐색. i=1 열 탐색
    start, end = 0, N-1
    M = -1
    while start <= end:
        mid = (start+end)//2
        if data[mid*(1-i)+y*i][mid*i]=='#': # i=0 일떈, 행 탐색. i=1 일땐, 열 탐색
            start = mid + 1
            M = mid
        else:
            end = mid - 1
    y = M # y값 갱신
    print(M, end=' ')


# y축 탐색
# start, end = 0, N-1
# Max = -1
# while start <= end:
#     mid = (start+end)//2
#     if data[mid][0]=='#':
#         start = mid + 1
#         Max = mid
#     else:
#         end = mid - 1

# # 해당 y행의 x축 탐색
# y = Max
# start, end = 0, N-1
# Max = -1
# while start <= end:
#     mid = (start+end)//2
#     if data[y][mid]=='#':
#         start = mid + 1
#         Max = mid
#     else:
#         end = mid - 1
# print(y, Max)