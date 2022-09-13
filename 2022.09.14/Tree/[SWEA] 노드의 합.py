t = int(input())
for case in range(1,t+1):
    N, M, L = map(int, input().split())
    arr = [0]*(N+1)
    for _ in range(M):
        node_idx, val = map(int, input().split())
        arr[node_idx] = val

    def traversal_tree(node):
        if node > N: return
        traversal_tree(node*2)
        traversal_tree(node*2+1)
        if node > 1: arr[node//2]+=arr[node]

    traversal_tree(1)
    print(f'#{case} {arr[L]}')

'''
test case
3
5 3 2
4 1
5 2
3 3
10 5 2
8 42
9 468
10 335
6 501
7 170
17 9 4
16 479
17 359
9 963
10 465
11 706
12 146
13 282
14 828
15 962
'''