t = int(input()) # 테스트 케이스 갯수
for c in range(t):
    k, n, m = map(int, input().split())
    stops = list(map(int, input().split()))
    cur = 0
    next = cur + k
    cnt = 0
    while next!=n: # next가 마지막인 경우 멈춤
        if next == cur: # 불가능한 케이스
            cnt=0
            break
        if next in stops: # next가 충전소 목록에 있는 경우 
            cur = next
            next = cur + k
            cnt += 1
        else:
            next -= 1
    print(f'#{c+1} {cnt}')