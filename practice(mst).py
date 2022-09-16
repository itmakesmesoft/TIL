'''
5 
8 
C D 1
A B 9
A C 3
A E 7
B D 11
A D 20
B C 14
C E 5
'''

# N = int(input()) # 정점의 개수
# M = int(input()) # 간선의 개수
# arr = []
# lst = [0]*200
# costs = 0
# for _ in range(M):
#     a, b, cost = input().split()
#     cost = int(cost)
#     arr.append([a,b,cost])
# arr = sorted(arr, key=lambda x:x[2])
    
# def find_boss(member): # 보스 반환
#     global lst
#     if lst[ord(member)]==0:
#         return member
#     ret = find_boss(lst[ord(member)])
#     lst[ord(member)]=ret
#     return ret

# def union(a, b, cost):
#     global lst, costs
#     fa, fb = find_boss(a), find_boss(b)
#     if fa == fb: return # 보스가 같은 경우 스킵
#     # print(a, b, cost)
#     costs += cost
#     lst[ord(fb)]=fa

# for i in range(M):
#     union(arr[i][0], arr[i][1], arr[i][2])
# print(costs)


# k = int(input()) # 정점의 갯수
# n = int(input()) # 간선의 갯수
# lst = [list(input().split()) for _ in range(n)]
# lst.sort(key=lambda x:int(x[2])) 
# costs = 0
# arr = [0]*200

# def union(a, b):
#     global arr
#     arr[ord(b)] = a

# def find(x):
#     global arr
#     if arr[ord(x)] == 0:
#         return x
#     ret = find(arr[ord(x)])
#     arr[ord(x)] = ret
#     return ret


# for i in range(n):
#     a, b, cost = lst[i]
#     fa, fb = find(a), find(b)
#     if fa != fb:
#         union(a, b)
#         costs += int(cost)
# print(costs)



