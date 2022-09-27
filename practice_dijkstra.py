# 가중치가 음수인 경우 다익스트라 알고리즘 사용할 수 없음 => 벨만 포드 알고리즘 이용
# 최소비용 구하는 알고리즘
# 시간복잡도 : O(n^2) => O(nlogn)
# 시작점 -> 도착점 바로 가는 비용과, 시작-> 경유-> 도착 가는 비용을 비교해서
# result 리스트에 저렴한 비용으로 갱신

# used리스트 체크
# result = 시작점 -> 도착점 비용으로 초기화
# 경유지 선택
# 1. 경유지 선택
# 2. used==0인지 체크
'''
inf = int(21e8)
arr = [
    [0, 3, inf, 9, 5],
    [inf, 0, 7, inf, 1],
    [inf, inf, 0, 1, inf],
    [inf, inf, inf, 0, inf],
    [inf, inf, 1, inf, 0],
]
n = len(arr)
used = [0]*n
result = [0]*n
start, end = map(int, input().split())
for i in range(n):
    result[i] = arr[start][i]
used[start]=1


def select_via(): # 사용되지 않은 원소 중 가장 작은 원소를 via로 선택
    Min = int(21e8)
    for i in range(n):
        if used[i]==0 and result[i] < Min:
            Min = result[i]
            Minindex = i
    return Minindex

def dijkstra():
    for i in range(n-1):
        via_idx = select_via() # 경유할 포인트 선정
        used[via_idx] = 1
        for j in range(n):
            direct = result[j] 
            via = result[via_idx] + arr[via_idx][j]
            if direct > via:
                result[j]=via
        print(*result)

dijkstra()
# print(*result)
'''


# 개선된 버전의 다익스트라 알고리즘(힙큐 이용)
'''
5 정점의 개수
7 간선의 개수
0 1 3 시작점, 도착점, 비용
0 3 9
0 4 5
1 2 7
1 4 1
2 3 1
4 2 1
0 3 시작점, 알고자 하는 도착점()
'''

import heapq

def dijkstra(start):
    # heapq.heappush(heap, (비용, 경유노드))
    heapq.heappush(heap, (0, start)) # 처음에는 시작노드를 경유노드로 놓기 
    result[start]=0                  # 그 다음 부터는 heapq에서 최소 비용을 다음 경유노드로 선택

    while heap:
        dist, node = heapq.heappop(heap)  
        # dist : 시작노드에서 경유노드 까지 비용
        # node : 경유 노드

        if result[node] < dist: continue    
        # result에 업데이트 된 비용(시작->경유)과 큐에서 뽑은 비용(시작->경유)을 비교
        for next in arr[node]:     # 모든 정점에 대해서 (경유지에서 도착할 수 있는 정점) 비교
            cost = dist+next[1]    
            # cost : 비용(시작->경유) + 비용(경유->도착)
            # next : [0: 노드, 1: 비용]
            if cost < result[next[0]]:
                result[next[0]] = cost
                heapq.heappush(heap, (cost, next[0]))

name = 'ABCDE'
n = int(input())
m = int(input())
arr = [[] for _ in range(n)]
for _ in range(m): # 인접 리스트 만들기
    a,b,c = map(int, input().split()) # 시작, 도착, 비용
    arr[a].append((b, c))
start, end = map(int, input().split())
inf = int(21e8)
result = [inf]*n    # 각 노드별 최소비용을 저장할 result 리스트 초기화
heap = []
dijkstra(start)
print(*result)

'''
5
7
0 1 3
0 3 9
0 4 5
1 2 7
1 4 1
2 3 1
4 2 1
0 3
'''