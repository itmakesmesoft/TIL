# union find 알고리즘
# 각각의 독립된 데이터를 그룹화 시켜 자료들을 관리할 때 사용되는 알고리즘
'''
def find(node):
    if parents[node] == node:
        return node
    ret = find(parents[node]) # 재귀적으로 부모 노드 탐색
    parents[node] = ret # 부모 노드 갱신
    return ret # 부모 노드 반환

def union(a, b):
    global parents
    p_a, p_b = find(a), find(b)
    if p_a == p_b: return True
    parents[p_b] = p_a


n = int(input()) # 간선 갯수
edge = [list(map(int, input().split())) for _ in range(n)] # 간선 정보
parents = list(range(3))

for i in range(n):
    a, b = edge[i]
    if union(a,b):
        print("사이클 발견")
        break
else:
    print("미발견")
'''





# minimum spanning tree (최소신장트리)
# 크루스칼 알고리즘

# 입력 후 비용을 기준으로 sort
# 간선의 개수 만큼 for문 돌리면서 union 하기
# 단 그룹화를 (간선의개수-1)개 시키는데..
# 그룹화에 성공을 하면 비용을 더해준다.
# 이미 같은 그룹이면 넘어가기!!!


'''
5       # 정점의 개수
8       # 간선의 개수
C D 1   # 간선의 정보 입력
A B 9
A C 3
A E 7
B D 11
A D 20
B C 14
C E 5
'''

# 개전 전 코드
'''
N = int(input()) # 정점의 개수
M = int(input()) # 간선의 개수
arr = []
lst = [0]*200
costs = 0
for _ in range(M):
    a, b, cost = input().split()
    cost = int(cost)
    arr.append([a,b,cost])
arr = sorted(arr, key=lambda x:x[2])
    
def find_boss(member): # 보스 반환
    global lst
    if lst[ord(member)]==0:
        return member
    ret = find_boss(lst[ord(member)])
    lst[ord(member)]=ret
    return ret

def union(a, b, cost):
    global lst, costs
    fa, fb = find_boss(a), find_boss(b)
    if fa == fb: return # 보스가 같은 경우 스킵
    # print(a, b, cost)
    costs += cost
    lst[ord(fb)]=fa

for i in range(M):
    union(arr[i][0], arr[i][1], arr[i][2])
print(costs)
'''


# 개선 후 코드
'''
k = int(input()) # 정점의 갯수
n = int(input()) # 간선의 갯수
lst = [list(input().split()) for _ in range(n)]
lst.sort(key=lambda x:int(x[2])) 
costs = 0
arr = [0]*200

def union(a, b):
    global arr
    arr[ord(b)] = a

def find(x):
    global arr
    if arr[ord(x)] == 0:
        return x
    ret = find(arr[ord(x)])
    arr[ord(x)] = ret
    return ret

for i in range(n):
    a, b, cost = lst[i]
    fa, fb = find(a), find(b)
    if fa != fb:
        union(a, b)
        costs += int(cost)
print(costs)
'''
