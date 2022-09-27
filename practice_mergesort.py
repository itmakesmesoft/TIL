def merge_sort(arr):
    if len(arr) == 1: # 더 이상 나누어 지지 않는 경우 arr을 반환
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(l_list, r_list):
    tmp = []
    l_pointer = r_pointer = 0 # 왼쪽 리스트의 인덱스, 오른쪽 리스트의 인덱스

    while l_pointer<len(l_list) and r_pointer<len(r_list):
        if l_list[l_pointer] < r_list[r_pointer]:
            tmp.append(l_list[l_pointer])
            l_pointer+=1
        else:
            tmp.append(r_list[r_pointer])
            r_pointer+=1
    
    # extend 함수를 통해 남은 원소를 tmp에 병합
    tmp.extend(l_list[l_pointer:])
    tmp.extend(r_list[r_pointer:])

    return tmp

arr = [231,234,1,4323, 65,32, 345]
merge_sort(arr)
print(arr)