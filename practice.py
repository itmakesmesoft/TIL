# def function(param):
#     res=""
#     cnt=0 # 가장 첫번째 대문자는 바꾸지 않기 위해 카운트 변수 설정
#     for p in param:
#         if p.isalpha():
#             if p.isupper() and cnt==0: # 문자가 대문자이고, cnt가 0인 경우
#                 res+=p #그대로 대문자를 출력하고
#                 cnt=1  #cnt=1로 대입
#             else:
#                 res+=p.lower()
#         else:
#             if p in [',','.','\'']:
#                 res+=p
#     return res

# print(function(input()))



# def sum_of_repeat_number(param):
#     res=[]
#     for p in param:
#         if param.count(p)==1:
#             res.append(p)
#     return sum(res)


# arr=list(map(int, input().split())) #입력 예시 3 4 5 23 3 4
# print(sum_of_repeat_number(arr))




# words_dict = {'proper' : '적절한',
# 'possible' : '가능한',
# 'moral' : '도덕적인',
# 'patient' : '참을성 있는',
# 'balance' : '균형',
# 'perfect' : '완벽한',
# 'logical' : '논리적인',
# 'legal' : '합법적인',
# 'relevant' : '관련 있는',
# 'responsible' : '책임감 있는',
# 'regular' : '규칙적인'}


# def function(param):
#     res=[]
#     for word in param:
#         if word[0] in ['b','m','p']:
#             res.append('im'+word)
#         elif word[0] == 'l':
#             res.append('il'+word)
#         elif word[0] == 'r':
#             res.append('ir'+word)
#         else:
#             res.append('in'+word)
#     res.sort()
#     return res

# print(function(words_dict))

# 1.
# def count_vowels(param):
#     count=0
#     for vowel in ['a','e','i','o','u']:
#         count+=param.count(vowel)
#     return count
# word=input()
# print(count_vowels(word))

# # 2.
# answer : (4)

# # 3. 
# def only_square_area(widths, heights):
#     res=[]
#     for i in widths:
#         if i in heights:
#             res.append(i**2)
#     return res
# widths=[32,55,63]
# heights=[13,32,40,55]
# print(only_square_area(widths, heights))



# T  = int(input())
# for testcase in range(1,T+1):
#     N = int(input())
#     snail = [[0] * N for _ in range(N)]
#     dy = [0, 1, 0, -1]
#     dx = [1, 0, -1, 0]
#     Y,X = 0,0
#     INDEX,num =0,1

#     while num <= N*N:
#         snail[Y][X] = num
#         num += 1
#         Y += dy[INDEX]
#         X += dx[INDEX]
#         if snail[Y][X] !=0 or Y < 0 or X < 0 or Y > N-1 or X > N-1:
#             Y -= dy[INDEX]
#             X -= dx[INDEX]
#             INDEX = (INDEX + 1) % 4
#             Y += dy[INDEX]
#             X += dx[INDEX]

#     print(f'{testcase}')
#     for i in range(N):
#         for j in range(N):
#             print(snail[i][j],end = '')
#         print()




# def dfs(level, start):
#     global path
#     if level == 3:
#         print(*path)
#         return

#     for i in range(start, len(arr)):
#         path[level] = arr[i]
#         dfs(level+1, i)
#         path[level] = 0

# arr = list(input())
# path = [0]*3 # [0, 0, 0]
# dfs(0, 0)




def bomb(y, x):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    for i in range(4):
        k = 1
        while True:
            ny, nx = y+dy[i]*k, x+dx[i]*k
            if ny>n-1 or nx>n-1 or ny<0 or nx<0: break
            if arr[ny][nx]==3: break
            arr[ny][nx]=2
            k+=1

# arr = [
#     [0,0,3,0,0],
#     [0,3,1,0,3],
#     [0,3,1,0,3],
#     [3,0,0,1,0],
#     [0,3,1,0,3]
# ]
arr = [
    [0,0,0,0,0],
    [0,1,3,1,0],
    [0,3,0,3,0],
    [0,1,3,1,0],
    [0,0,0,0,0]
]

n = len(arr)
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            bomb(i, j)
cnt =0
for i in range(n):
    for j in range(n):
        if arr[i][j]==0:
            cnt+=1
print(cnt)

'''
test case
arr = [
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,3,0,3,0],
    [0,1,3,1,0],
    [0,0,0,0,0]
]
'''