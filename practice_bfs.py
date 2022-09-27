# 데크 모듈 이용 BFS 구현
# 0. 데크 특징
#   - O(1)의 시간복잡도로 양방향 삽입 삭제 가능
'''
q = deque()     # 데크 생성
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)
print(*q)       # 2 3 4 5 6
q.appendleft(9) # 양방향 추가 가능
print(*q)       # 9 2 3 4 5 6
x = q.popleft()
print(x)        # 9
print(*q)       # 2 3 4 5 6
y = q.pop()
print(y)        # 6
print(*q)       # 2 3 4 5

'''


# 데크 모듈 사용법
# 1. 인접리스트 생성
# 2. 데크 생성
# 3. 데크에 현재 갈 수 있는 인덱스를 append
# 4. 데크에서 popleft해서 now에 넣고, now인덱스에서 갈 수 있는 인덱스를 다시 데크에 append
# 5. 배열을 마치면 path에 현재 인덱스 방문 처리


# 예시 1.
# '''
#    A
#  B   C
# D E   F

# '''
# from collections import deque # 데크 모듈 import
# arr = [
#     [0,1,1,0,0,0],
#     [0,0,0,1,1,0],
#     [0,0,0,0,0,1],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
# ]
# def bfs(st):
#     global answer
#     q = deque()
#     q.append(st)
#     while q:
#         now = q.popleft()
#         answer.append(chr(now+65))
#         for i in range(len(arr)):
#             if arr[now][i]==1:
#                 q.append(i)
# answer = []
# bfs(0)
# print(answer)






# 예시 2.
# from collections import deque
# def bfs(start):
#     global path, visited
#     q = deque()
#     q.append(start)
#     while q:
#         now = q.popleft()
#         path.append(chr(now+65))
#         for i in range(len(arr)):
#             if arr[now][i]==1 and visited[i]==0:
#                 visited[i]=1
#                 q.append(i)

# arr = [
#     [0,1,1,0],
#     [0,0,1,1],
#     [0,1,0,1],
#     [0,0,0,0],
# ]
# start = int(input())
# visited = [0]*len(arr)
# visited[start] = 1
# path = []
# bfs(start)
# print(*path)






# 예시 3. 
# < flood fill/Bloom/Virus 유형 >
# '''
# 시작점 (1, 1)을 기준으로 상하좌우로 +1씩 더해져 입력
# [
#     [3,2,3,4],
#     [2,1,2,3],
#     [3,2,3,4],
#     [4,3,4,5],
# ]
# '''
# from collections import deque

# N = int(input()) # 맵 사이즈
# y, x = map(int, input().split()) # 꽃이 피기 시작하는 시작점
# arr = [[0]*N for _ in range(N)]
# arr[y][x] = 1

# q = deque()
# q.append([y, x])
# while q:
#     now = q.popleft()
#     y,x = now
#     dy = [0,1,0,-1]
#     dx = [1,0,-1,0]
#     for i in range(4):
#         ny, nx = y+dy[i], x+dx[i]
#         if ny > N-1 or nx > N-1 or ny < 0 or nx < 0: continue
#         if arr[ny][nx]!=0: continue
#         arr[ny][nx] = arr[y][x] + 1
#         q.append([ny, nx])

# for i in range(N): # 출력
#     print(*arr[i])
# '''
# test case
# 3
# 1 1

# 5
# 2 1
# '''






# 예시 4. 
# from collections import deque

# def bfs(y, x):
#     global Map
#     q = deque()
#     q.append([y, x])
#     while q:
#         now = q.popleft()
#         y, x = now
#         dy = [0,1,0,-1]
#         dx = [1,0,-1,0]
#         for i in range(4):
#             ny, nx = y+dy[i], x+dx[i]
#             if ny>n-1 or nx>n-1 or ny<0 or nx<0: continue
#             if Map[ny][nx]!=0: continue
#             if ny == nx and ny == 0:
#                 return Map[y][x]
#             Map[ny][nx] = Map[y][x]+1
#             q.append([ny, nx])


        
# n = int(input())
# y, x = map(int, input().split())
# Map = [[0]*n for _ in range(n)]
# Map[y][x] = 1
# print(f'{bfs(y, x)}일 후')
# '''
# test case
# 5
# 3 1

# 8
# 7 3
# '''





# # 예시 5. 화단에 씨앗이 심길 위치 2곳을 입력받고 
# # 화단에 꽃이 모두 개화하는데 몇 일이 걸릴지 출력하라
# from collections import deque
# def bfs(lst):
#     global arr
#     q = deque()
#     for i in range(len(lst)):
#         q.append(lst[i])
#     while q:
#         now = q.popleft()
#         y, x = now
#         dy = [0,1,0,-1]
#         dx = [1,0,-1,0]
#         for i in range(4):
#             ny, nx = y+dy[i], x+dx[i]
#             if ny>n-1 or nx>n-1 or ny<0 or nx<0: continue
#             if arr[ny][nx] != 0: continue
#             arr[ny][nx] = arr[y][x]+1
#             days=arr[y][x]
#             q.append([ny, nx])
#     return days

# n = int(input())
# lst = [[1,3],[5,6]]
# arr = [[0]*n for _ in range(n)]
# for y, x in lst:
#     arr[y][x]=1

# print(f'{bfs(lst)}일 후')
# # for i in range(n): # 그래프 출력
# #     print(*arr[i])






# 예시 6. 미로찾기
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