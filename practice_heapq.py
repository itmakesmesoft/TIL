'''
import heapq # 우선순위 큐를 사용하기 위한 모듈
# heapq는 삽입 삭제가 O(logn) 속도

arr = [] # 모듈함수를 사용할 때 arr 리스트에 인자 값을 담음

heapq.heappush(arr, 4) # 최소힙 디폴트 => 값이 가장 작은 것이 우선순위가 높음
heapq.heappush(arr, 445)
heapq.heappush(arr, 43)
heapq.heappush(arr, 13)
heapq.heappush(arr, 123)

print(arr) # [4, 13, 43, 445, 123]

# print(heapq.heappop(arr)) # O(logn)의 속도로 우선순위가 가장 높은 값 출력
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))

for i in range(len(arr)):
    print(heapq.heappop(arr))
'''


# 기존의 리스트를 힙 자료구조로 바꾸기
# 방법 1. 빈 리스트 생성 후 heappush로 원소 삽입
'''
import heapq

lst = [123,346,345,63,452,35,54,31,1,23]
heap = []
for i in range(len(lst)):
    heapq.heappush(heap, lst[i])

for i in range(len(heap)):
    print(heapq.heappop(heap))
'''
# 방법 2. heapify(list)를 이용하여 힙 구조로 변환
'''
import heapq

lst = [123,346,345,63,452,35,54,31,1,23]
heapq.heapify(lst) # heap 자료형으로 바꾸기
'''

# Max Heap 구현하기
# 방법 1.
'''
import heapq

arr = [4,354,3,8,4,7,65,13,54]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap, -arr[i]) # -354, -65, ...
print(heap)                                  # heap 자료 내부에는 음수값이 저장
for i in range(len(arr)):
    print(heapq.heappop(heap)*(-1), end=' ') # pop과정에서 음수를 곱해 양수값을 출력시킴
    # == print(-heapq.heappop(heap)) 위와 같은 동작을 함
'''

# 방법 2. 람다 함수 이용 (오류 있음)
'''
import heapq

arr = [4,354,3,8,4,7,65,13,54]
rev = lambda x:x*-1
heap = list(map(rev, arr))
heapq.heapify(heap)
for i in range(len(arr)):
    print(-heapq.heappop(heap), end=' ')
'''

# 방법 3. 튜플 이용
'''
import heapq

arr = [4,354,3,8,4,7,65,13,54]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap, (-arr[i], arr[i]))

for i in range(len(arr)):
    print(heapq.heappop(heap)[1])
'''



# 우선순위 큐 문제

# 1. 카드 정렬하기
# 정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 
# 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다. 
# 이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.
# 매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 
# 고르는 순서에 따라서 비교 횟수가 매우 달라진다. 

# 예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 
# 합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다. 
# 그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.
# N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.


# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다. 숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.


# 출력
# 첫째 줄에 최소 비교 횟수를 출력한다.

# 입력
'''
4
50
20
70
30
'''
# 출력
# 320

# 나의 풀이
# import heapq

# n = int(input())
# heap = []
# for i in range(n):
#     heapq.heappush(heap, int(input()))
# total = heapq.heappop(heap) + heapq.heappop(heap)
# for i in range(2, n):
    
# print(total)

# 정답 풀이
import heapq
n=int(input())
card=[]

for i in range(n):
    heapq.heappush(card,int(input()))

answer=0
while len(card)>1:
    temp1=heapq.heappop(card)
    temp2=heapq.heappop(card)
    answer+=(temp1+temp2)
    heapq.heappush(card,temp1+temp2)

print(answer)