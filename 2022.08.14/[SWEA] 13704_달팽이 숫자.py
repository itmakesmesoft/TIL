t = int(input())
for c in range(t):
    n = int(input())
    arr = [[0]*n for _i in range(n)]
    direct = [[0,1],[1,0],[0,-1],[-1,0]]
    y, x = 0, -1
    i=0
    for num in range(1, n**2+1):
        tmp_y, tmp_x = y+direct[i][0], x+direct[i][1] # 조건문 판단을 위해 tmp 생성 
        if tmp_x>n-1 or tmp_y>n-1 or tmp_x<0 or tmp_y<0 or arr[tmp_y][tmp_x]!=0: # 범위를 벗어나거나 0인 경우 방향 전환
            i+=1
            i=i%4
        y+=direct[i][0] #y 갱신
        x+=direct[i][1] #x 갱신
        arr[y][x]=num
    print(f'#{c+1}') # 출력
    for k in range(n):
        print(*arr[k])
