def partition(left, right):
    pivot = arr[left]   # 피봇을 배열의 가장 왼쪽 값으로 초기화
    i, j = left, right  

    while i <= j:       # i, j 가 교차 시, i, j는 피봇을 기준으로 작은 값과 큰 값들의 경계에 위치
                        
        while i <= j and arr[i] <= pivot: # i : 왼쪽에서 오른쪽 방향으로 피봇보다 큰 값을 탐색
            i += 1
        while i <= j and arr[j] >= pivot: # j : 오른쪽에서 왼쪽 방향으로 피봇보다 큰 값을 탐색
            j -= 1
        
        if i < j :      # i와 j가 결정된 이후, arr[i]와 arr[j]를 SWAP
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[left], arr[j] = arr[j], arr[left]
    
    return j

def quick_sort(left, right):
    if left < right: # 시작 인덱스보다 끝 인덱스가 큰 경우
        mid = partition(left, right)
        quick_sort(left, mid-1)
        quick_sort(mid+1, right)

arr = [7, 2, 5, 3, 4, 5]
n = len(arr)
quick_sort(0, n-1) # 시작 인덱스와 끝 인덱스를 인자로 전달
print(arr)


