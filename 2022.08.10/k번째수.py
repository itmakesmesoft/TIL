def solution(array, commands):
    answer=[]
    for command in commands:
        i, j, k = command
        arr = array[i-1:j]
        
        n=j-i+1 # arr 원소의 갯수
        for i in range(n): #버블정렬
            for j in range(n-1):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        answer.append(arr[k-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))