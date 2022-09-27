
# BFS 심화
# 문제 1. 미로 찾기
# bfs 2번사용

# from collections import deque

# arr = [ # 0: 가능(도로) | 1: 불가능(벽)
#     [0,0,0,1,1],
#     [0,0,0,1,0],
#     [1,0,0,0,0],
#     [0,0,0,0,0],
# ]

# def bfs(sty, stx, eny, enx):
#     visited = [[0]*5 for _ in range(4)]
#     visited[sty][stx] = 1
#     q = deque()
#     q.append((sty, stx, 0)) # start_y, start_x, level
#     while q:
#         now = q.popleft()
#         y, x, level = now
#         if y==eny and x == enx: break # 목적지 도착 시 break
#         dy= [-1,0,1,0]
#         dx= [0,-1,0,1]
#         for i in range(4):
#             ny, nx = y+dy[i], x+dx[i]
#             if ny > 3 or nx > 4 or ny < 0 or nx < 0: continue
#             if arr[ny][nx]==1: continue # 벽인 경우 continue
#             if visited[ny][nx]==1: continue # 방문한 경우 continue
#             visited[ny][nx]=1
#             q.append((ny, nx, level+1))
#     return level

# ret = bfs(0, 0, 3, 0) + bfs(3, 0, 3, 4) # bfs(start_y, start_x, end_y, end_x)
# print(ret)



# 문제 2. 섬의 크기 구하기
# BFS 시작점 = 섬의 시작점 <= for문을 처음 값이 1이 되는 부분을 시작점으로 설정

# from collections import deque

# def bfs(y, x):
#     global visited
#     q = deque()
#     q.append([y, x])
#     size = 0
#     while q:
#         size += 1 # 섬 크기 size+1
#         now = q.popleft()
#         y, x = now
#         dy = [0,1,0,-1]
#         dx = [1,0,-1,0]
#         for i in range(4):
#             ny, nx = y+dy[i], x+dx[i]
#             if ny > N-1 or nx > N-1 or ny< 0 or nx < 0: continue
#             if visited[ny][nx] == 1: continue
#             if arr[ny][nx]==0: continue
#             visited[ny][nx] = 1
#             q.append([ny, nx])
#     return size



# arr = [ # 1: 섬 | 0: 바다
#     [0,0,1,0,0],
#     [0,0,1,0,0],
#     [0,1,1,1,0],
#     [0,0,1,0,0],
#     [1,0,0,0,1],
# ]
# N = len(arr) # int(input())

# cnt = 0
# visited = [[0]*N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if arr[i][j]==1 and visited[i][j]==0:
#             visited[i][j] = 1
#             cnt+=1 # 섬의 갯수 +1
#             print(f'{cnt}번 째 섬 크기 : {bfs(i, j)}')
# print(f'섬의 총 갯수 : {cnt}')



from collections import deque

def bfs(start_y, start_x, end_y, end_x):
    visited = [[0]*6 for _ in range(4)]
    visited[start_y][start_x] = 1
    q = deque()
    q.append([start_y, start_x, 0, 2]) # start_y, start_x, level, destroy(파괴 가능한 벽 수)
    while q:
        now = q.popleft()
        y, x, level, destroy = now
        if y == end_y and x == end_x: break
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>3 or nx>5 or ny<0 or nx<0: continue   # 범위를 벗어난 경우
            if visited[ny][nx]==1: continue
            if arr[ny][nx]==0:                          # 길인 경우
                q.append([ny, nx, level+1, destroy])
                visited[ny][nx]=1
            else:                                       # 벽을 만난 경우
                if destroy > 0:                         # 파괴 가능한 경우가 0 이상인 경우
                    q.append([ny, nx, level+1, destroy-1])
                    visited[ny][nx]=1
    return level

arr = [
    [0,0,1,1,1,1],
    [0,0,1,0,0,1],
    [0,0,1,0,1,1],
    [0,0,1,0,1,0],
]
start_y, start_x = 0, 0
end_y, end_x = 3, 5
print(bfs(start_y, start_x, end_y, end_x))