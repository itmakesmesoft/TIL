# Topology Sort(위상 정렬)
# 그래프에 사이클이 있는 경우 사용 못함
# union-find를 통해 사이클이 없는지 확인 후 사용
'''
F       H     
A           G
    C - E
B
    D

인접 행렬
  A B C D E F G H
A 0 0 1 0 0 0 0 0
B 0 0 1 0 0 0 0 0
C 0 0 0 0 1 0 0 0
D 0 0 0 0 1 0 0 0
E 0 0 0 0 0 0 1 0
F 0 0 0 0 0 0 0 1
G 0 0 0 0 0 0 0 0
H 0 0 0 0 0 0 1 0

        A B C D E F G H
ACC  = [0,0,2,0,2,0,2,1] # 필요한 사전 작업갯수
USED = [1,1,0,1,0,1,0,0] 
Q = [A, B, D, F]
'''

from collections import deque

name = ['cs', 'language', 'datastructure', 'algorithm', 'project', 'condingtest', 'programmer']
arr = [
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
]

acc = [0]*7
used = [0]*7
q = deque()

for i in range(7): # 사전 작업 개수 등록
    for j in range(7):
        if arr[j][i]==1:
            acc[i]+=1

for i in range(7):
    if acc[i]==0: # 사전 작업 개수가 0인 경우
        q.append(i) # q.append 후 used 체크
        used[i]=1

while q:
    now = q.popleft()
    print(name[now])
    for i in range(7):
        if arr[now][i]==1 and used[i]==0:
            if acc[i]==1:
                used[i]=1
                q.append(i)
                acc[i]-=1
            else:
                acc[i]-=1