# Binary Search
# 정렬된 리스트만 가능


N = int(input())
books = list(input().split())

for i in range(N):# 사전순 정렬
    min_i = i
    for j in range(i+1, N):# 선택 정렬
        if books[j] < books[min_i]:
            min_i = j
    books[i], books[min_i] = books[min_i], books[i]

M = int(input())
for _ in range(M):
    book, s = input().split()
    s = int(s)  # BS 이용 책 검색
    cnt = 0
    flag = 0    # 0: 못찾음 | 1: 찾음
    start, end = 0, N-1
    while start <= end and cnt < s:
        mid = (start+end)//2
        if books[mid]==book:
            flag = 1
            break
        if books[mid]>book:
            end = mid-1
        else:
            start = mid+1
        cnt += 1

    if flag:
        print("pass")
    else:
        print("fail")

'''
6
Rabbit Moon Opening Alien Power Ai
3
Opening 5
Alien 1
Ai 3

'''