N, M = map(int, input().split())
li=[]
for _ in range(N):
    li.append(list(input()))
arr_w=[[0]*M for _ in range(N)]
arr_b=[[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if (i%2==0 and j%2==1) or (i%2==1 and j%2==0):
            if li[i][j]=='W':
                arr_b[i][j]=1
            else:
                arr_w[i][j]=1
        else:
            if li[i][j]=='W':
                arr_w[i][j]=1
            else:
                arr_b[i][j]=1
res=[]
for i in range(N-7):
    for j in range(M-7):
        w=0
        b=0
        for k in arr_w[i:i+8]:
            w+=sum(k[j:j+8])
        for l in arr_b[i:i+8]:
            b+=sum(l[j:j+8])
        res.append(w)
        res.append(b)
print(min(res))
