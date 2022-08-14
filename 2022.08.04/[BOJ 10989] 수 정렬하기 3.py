import sys
n=int(input())
arr=[0 for _ in range(10001)]
for i in range(n):
    arr[int(sys.stdin.readline())]+=1
for k, i in enumerate(arr):
    for _ in range(i):
        print(k)