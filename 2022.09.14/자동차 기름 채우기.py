# Binary Search
# 정렬이 된 리스트여야 함

gage = list(input()) # 10글자

start, end = 0, 9
Max = -1
while start <= end:
    mid = (start+end)//2
    if gage[mid]=='#':
        start = mid + 1
        Max = mid
    elif gage[mid]=='_':
        end = mid - 1
print(f'{(Max+1)*10}%')


'''
test case
######____

##________

#_________

#########_

__________
'''