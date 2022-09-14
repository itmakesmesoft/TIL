# Binary Search
# 이진탐색은 반드시 정렬된 데이터에서만!
target = int(input())

arr = [4,4,5,7,8,10,20,22,23,24]
start, end = 0, len(arr)-1
flag = 0

while start<=end:
    mid = (start+end)//2
    if arr[mid]==target: 
        flag = 1
        break
    elif arr[mid] > target:
        end = mid-1

    else:       # arr[mid] < target
        start = mid+1
print("O"*flag + "X"*(1-flag))
