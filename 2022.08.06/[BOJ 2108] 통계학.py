import sys
n=int(sys.stdin.readline())
arr=[] # 숫자를 담을 리스트 생성
dic={} # 숫자를 키로, 갯수를 밸류로 받을 딕셔너리 생성
for i in range(n):
    val=int(sys.stdin.readline())
    arr.append(val) # 숫자를 리스트에 추가
    if val not in dic: # 숫자가 딕셔너리에 있으면 +1, 없으면 1을 대입
        dic[val]=1
    else:
        dic[val]+=1
print(int(round(sum(arr)/n, 0))) # 산술평균
arr.sort() # 리스트를 오름차순으로 정렬
print(arr[n//2]) # 중앙값
res = sorted(dic.items(), key=lambda x:x[1])
result = [k for k, v in dic.items() if v==res[-1][1]]
print(sorted(result)[1]) if len(result)>1 else print(result[0]) # 최빈값
print(arr[-1]-arr[0]) # 범위(최대최소 차)