# n = int(input())
# pi = list(map(int,input().split()))

# def gettotal(path, m):
#     total = 0
#     for i in range(m+1):
#         total+=pi[path[i]]
#     return total

# def dfs(level):
#     global min_time, used, path
#     if level == n:
#         total = 0
#         for i in range(n):
#             total += gettotal(path, i)
#         if total < min_time:
#             min_time = total
#         return 
#     for i in range(n):
#         if used[i]==1: continue
#         used[i]=1
#         path[level]=i
#         dfs(level+1)
#         used[i]=0

# min_time = 21e8
# used = [0]*n
# path = [0]*n
# dfs(0)
# print(min_time)

# Greedy 기법 적용
# n= int(input())
# time_w = list(map(int, input().split())) # [4, 3, 3, 2, 1]

# time_w.sort(reverse=True)
# answer = 0
# for i in range(1, n+1):
#     answer+=(i*time_w[i-1]) 

# print(answer)

#================================================

# n = int(input())
# timelst = {}
# for i in range(n):
#     start, end = map(int, input().split())
#     if start not in timelst:
#         timelst[start]=[end]
#     else:
#         timelst[start].append(end)

# i=10
# cnt=0
# while i<=22:
#     if i in timelst:
#         timelst[i].sort()
#         i = timelst[i][0]
#         cnt+=1
#     else:
#         i+=1
# print(cnt)


#================================================


# # 회의실 배정
# '''
# 시작시간과 종료시간이 있는 n개의 활동들의 집합 A={A1, A2, ... An}에서 
# 서로 겹치지 않는 최대개수의 활동들의 집합 S를 구하는 문제

# Greedy 기법
# - 종료시간 순으로 활동을 정렬
# - 이전 종료타임 이후부터 배정 가능한 경우를 cnt
# '''

# n = int(input())
# timelst = [list(map(int, input().split())) for _ in range(n)]
# timelst.sort(key=lambda x:x[1])
# cnt = 0
# start = 0
# for i in range(n):
#     if start <= timelst[i][0]:
#         start = timelst[i][1]
#         cnt+=1
# print(cnt)


#=====================================
# 최소 거리 비용 구하기
# arr = [
#     [0,1,1,9],
#     [4,2,2,3],
#     [1,3,4,1],
#     [3,7,8,0]
# ]
# n = len(arr)

# for i in range(n):
#     for j in range(n):
#         if i > 0 or j > 0:
#             if i == 0:
#                 arr[i][j]+=arr[i][j-1]
#             elif j == 0:
#                 arr[i][j]+=arr[i-1][j]
#             else:
#                 if arr[i][j-1]>arr[i-1][j]:
#                     arr[i][j]+=arr[i-1][j]
#                 else:
#                     arr[i][j]+=arr[i][j-1]
# print(arr[n-1][n-1])


# 다른 풀이
# arr = [
#     [0,1,1,9],
#     [4,2,2,3],
#     [1,3,4,1],
#     [3,7,8,0]
# ]

# arr1 = [[0]*4 for _ in range(4)]

# for i in range(1,4):
#     arr1[0][i] = arr1[0][i-1]+arr[0][i]
#     arr1[i][0] = arr1[i-1][0]+arr[i][0]

# for i in range(1,len(arr)):
#     for j in range(1,len(arr)):
#         arr1[i][j] = min(arr1[i-1][j],arr1[i][j-1]) + arr[i][j]

# print(arr1[3][3])


#----------------------------------------

# n, k = map(int, input().split())
# lst = [list(map(int, input().split())) for _ in range(n)]
# lst.sort(key=lambda x:x[0])
# arr = []
# for i in range(n):
#     total = lst[i][0]
#     total_w = lst[i][1]
#     for j in range(i):
#         if total+lst[j][0]<=k:
#             total+=lst[j][0]
#             total_w += lst[j][1]
#             arr.append(total_w)
# print(max(arr))


#---------------------------------------------


# knapsack(DP) 문제
# 물건이 1개 씩인 경우
'''
한 달 후면 국가의 부름을 받게 되는 정싸피는 여행을 가려고 한다. 
세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 
가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.
정싸피가 여행에 필요하다고 생각하는 N개의 물건이 있다. 
각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 정싸피가 V만큼 즐길 수 있다. 
아직 행군을 해본 적이 없는 정싸피는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
정싸피가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

<입력>
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 
두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 
해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
입력으로 주어지는 모든 수는 정수이며 제한시간은 2초 이다.

<출력>
한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

<제한조건>
단, 각 물건은 하나 씩만 있다.

<예시 입력>
4 7
6 13
4 8
3 6
5 12

<예시 출력>
14
'''

n, k = map(int, input().split())
lst=[[0, 0]]
for _ in range(n):
    lst.append(list(map(int, input().split())))
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        weight = lst[i][0]
        value = lst[i][1]
        if j < weight:  # 가방에 넣을 수 없으면
            dp[i][j] = dp[i - 1][j]  # 위에 값 그대로 가져오기
        else: # 가방에 넣을 수 있으면
            dp[i][j] = max(dp[i - 1][j], dp[i][j - weight] + value)
print(dp[n][k])



# ----------------------------------------------
# 동전교환 문제(DP)
# 동전이 무한 개인 경우

# k = 14
# coins = [1, 7, 10]
# table = [[0]*(k+1) for _ in range(len(coins))]
# for i in range(len(coins)):
#     for j in range(1, k+1):
#         if j//coins[i]>0:
#             rest = j - coins[i]*j//coins[i]
#             result = table[i][rest]+j//coins[i]
#             if result < table[i-1][j]:
#                 table[i][j] = result
#             else:
#                 table[i][j] = table[i][rest]+j//coins[i]
#         else:
#             if i>0:
#                 table[i][j] = table[i-1][j]
#             else:
#                 table[i][j] = j
# print(table)


# k = 14
# coins = [1, 7, 10]
# table = [[0]*(k+1) for _ in range(len(coins))]

# for i in range(len(coins)):  
#     for j in range(k + 1):  
#         if j%coins[i]==0: 
#             table[i][j]=j//coins[i]
#         else:
#             if j//coins[i]==0:
#                 table[i][j]=table[i-1][j]
#             else:
#                 table[i][j]=min(table[i-1][j], table[i][j%coins[i]])
# print(table[2][k])



# ==================================================



