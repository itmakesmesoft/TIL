# 1. 중복조합
# 각 항에서 1~4 사이의 숫자를 1개씩 택해서 다 더했을때 
# 10이 나오는 경우는 몇가지인지 출력
# (n개의 항에서 1~4 사이의 숫자 택)

# def dfs(num, total):
#     global cnt
#     if num == n:
#         if total == 10:
#             cnt += 1
#         return
#     for i in range(4):
#         dfs(num + 1, total + arr[i])

# arr = [1,2,3,4]
# n= int(input())
# cnt = 0
# dfs(0, 0)
# print(cnt)






# 2. 조합
# M, B, T, I 4명이 놀이동산에 갔다. 
# 놀이기구는 한 유닛에 3명이 앉을 수 있다
# 4명 중 1명이 고소공포증이 있어 놀이기구를 탑승하지 않는다고 한다.
# 놀이기구를 타는 모든 조합을 출력하라.

# def dfs(level, start):
#     global boarding
#     if level==3:
#         for i in range(4):
#             if boarding[i]==1:
#                 print(member[i], end=' ')
#         print()
#         return

#     for i in range(start, 4):
#         if boarding[i]==1: continue
#         boarding[i]=1
#         dfs(level+1, i+1)
#         boarding[i]=0

# member = ['M', 'B', 'T', 'I']
# boarding = [0]*4
# dfs(0, 0)






# 3. 순열
# line1=[3,7,1,-3,-6,1]
# line2=[7,-4,1,-5,3,2]
# 두 라인에서 숫자를 1개씩 번갈아 가며 선택을 하고자 한다. 
# 첫 번째 라인에서 숫자를 1개 택한 후 x1을 하고
# 두 번째 라인에서 숫자를 1개 택한 후 x2를 하고
# 첫 번째 라인에서 숫자를 1개 택한 후 x3을 하고..
# 두 번째 라인에서 숫자를 1개 택한 수 x4를 곱한다.
# 위와 같이 가중치가 1씩 증가되는 값으로 뽑은 숫자에 곱해 모두 더했을때 
# 0에 가장 가까운 총 합은 몇인가?
# (각 라인의 숫자는 1번 씩만 사용하여 모든 숫자를 한번씩 뽑는다.)

# def dfs(level, total):
#     global min_total
#     if level == 12:
#         if abs(total) < abs(min_total):
#             min_total = total
#         return
#     for i in range(6):
#         if level%2==0 and used[0][i]==0:
#             used[0][i]=1
#             dfs(level+1, total + line1[i]*(level+1))
#             used[0][i]=0
#         elif level%2==1 and used[1][i]==0:
#             used[1][i]=1
#             dfs(level+1, total + line2[i]*(level+1))
#             used[1][i]=0

# line1 = [3,7,1,-3,-6,1]
# line2 = [7,-4,1,-5,3,2]
# used = [[0]*6 for _ in range(2)]
# min_total = float('inf')
# dfs(0, 0)
# print(min_total)





# 4. 서바이벌 게임
# A ~ G 를 두팀으로 나누어서 게임을 하고자 한다.
# 두 팀으로 나누었을 경우, 두 팀의 전투력 차이의 최소값은 몇인가?
# (모든 선수는 경기에 참가를 하며 1인팀도 가능)
#           A   B   C   D   E   F   G
# power = [50, 40, 99,  5, 25,  6, 37]

# def dfs(level, tot):
#     global min_tot
#     if level == len(power)-1 : return
#     if abs(total - 2*tot) < abs(total - 2*min_tot):
#         min_tot = tot
#     for i in range(len(power)):
#         if used[i]==1: continue
#         used[i]=1
#         dfs(level+1, tot+power[i])
#         used[i]=0

# power = [50, 40, 99, 5, 25, 6, 37]
# total = sum(power)
# min_tot = float('inf')
# used = [0]*len(power)
# dfs(0, 0)
# print(abs(total-2*min_tot))





# 5. 
# '''
# test case
# 4
# 7 3 5 4
# '''

# def dfs(level, total):
#     global Max
#     if level == n:
#         if Max < total:
#             Max = total
#         return
#     dfs(level+1, total * (arr[level]*2))
#     dfs(level+1, total * (arr[level]//3))
#     dfs(level+1, total * (arr[level]+5))

# n = int(input())
# arr = list(map(int, input().split()))
# Max = float('-inf')
# dfs(0, 1)
# print(Max)


# 6. 땅파기 문제
# from copy import deepcopy
# arr = [
#     [4, 2, 1],
#     [5, 3, 9],
#     [7, 8, 1]
# ]

# def change(i, j):
#     global arr
#     dy = [0,0,1,0,-1]
#     dx = [0,1,0,-1,0]
#     for k in range(5):
#         ny, nx = i+dy[k], j+dx[k]
#         if ny > 2 or nx > 2 or ny < 0 or nx < 0: continue
#         arr[ny][nx] = (arr[ny][nx]*7)%10

# def getsum(array):
#     total = 0
#     for i in range(3):
#         for j in range(3):
#             total += array[i][j]
#     return total

# def dfs(level):
#     global Max, arr
#     backup = deepcopy(arr)
#     if level == 3:
#         total = getsum(arr)
#         if Max < total:
#             Max = total
#         return
#     for i in range(3):
#         for j in range(3):
#             change(i, j)
#             dfs(level+1)
#             arr = deepcopy(backup)
    
# Max = float('-inf')
# dfs(0)
# print(Max)