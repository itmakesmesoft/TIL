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