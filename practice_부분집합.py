# arr = [3,6,7,1,5,4]
# n = len(arr)

# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end=' ')
#     print()

# n = int(input())
# result = 1
# for i in range(1, n+1):
# 	result *= i
# print(result)



arr = [1,2,3,4]
n = len(arr)

for i in range(0, (1<<n)):  # 1<<n: 부분집합의 개수
    for j in range(0, n):   # 원소의 수만큼 비트를 비교
        if i & (1<<j):      # i의 j번째 비트가 1이면 j번째 원소 출력
            print('%d'%arr[j], end='')
    print()