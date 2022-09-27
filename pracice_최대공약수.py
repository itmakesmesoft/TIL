#### 최대공약수(Greatest Common Divisor)

# 원시적인 방법
'''
answer = 0
a, b = map(int, input().split())
for i in range(2, min(a,b)+1):
    if a%i==0 and b%i==0:
        answer=i
'''

# 개선된 방법(유클리도 호제법) => 최초의 알고리즘
'''
a, b = map(int, input().split())
answer = 0
while b:
    answer = a%b
    a=b
    b=answer
print(a)
'''



### 최소공배수(Least Common Multiple)
# 1. 최대공약수를 구한 뒤
# 2. LCM = GCD*(A/GCD)*(B/GCD) 최소공배수 공식을 대입
'''
a, b = map(int, input().split())
answer = 0
c, d = a, b
while d:
    answer = c%d
    c=d
    d=answer
LCM = c*a/c*b/c
print(LCM)
'''



### 소수 구하기(Prime Number)
# 소수 : 1과 자기 자신으로만 나눌 수 있는 수

# 원시적인 방법
'''
a = int(input())
flag = True
if a>2:
    for i in range(2, a):
        if a%i==0:
            flag = False
            break
if flag: print("소수")
else: print("소수 아님")
'''


# 개선된 방법(에라토스테네스의 체)
'''
n = int(input())
check = [True]*(n+1)
answer = []
for i in range(2, n+1): # 2부터 입력받은 수까지 확인
    if check[i]==True: answer.append(i)
    for j in range(i+i, n+1, i): # 확인하고자 하는 배수에 해당하는 값을 False
        check[j]=False
print(answer)
'''

# 더욱 개선된 방법(에라토스테네스의 체 순회 범위 축소)
import math

n = int(input())
check = [True]*(n+1)
answer = []
for i in range(2, int(math.sqrt(n))+1): # 2부터 입력받은 수까지 확인
    if check[i]==False: continue
    for j in range(i+i, n+1, i): # 확인하고자 하는 배수에 해당하는 값을 False
        check[j]=False
for i in range(2, n+1):
    if check[i]==True:
        answer.append(i)
print(answer)