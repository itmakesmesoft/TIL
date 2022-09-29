# 1. 애너그램 검증하기
'''
입력
flow wolf

출력
"애너그램"
'''
# string1, string2 = input().split()
# string1, string2 = sorted(list(string1)), sorted(list(string2))
# if string1 == string2:
#     print("애너그램")
# else:
#     print("애너그램 아님")




# 2. 애너그램을 만들기 위해서 제거해야할 문자 개수 세기
'''
입력
gbbgc aakscbb

출력
6
'''
# string1, string2 = input().split()
# bucket1, bucket2= [0]*200, [0]*200

# for i in range(len(string1)):
#     index = ord(string1[i])
#     bucket1[index]+=1
# for i in range(len(string2)):
#     index = ord(string2[i])
#     bucket2[index]+=1

# cnt = 0
# for i in range(200):
#     if bucket1[i]>0 or bucket2[i]>0:
#         val = abs(bucket1[i]-bucket2[i])
#         cnt += val
# print(cnt)



# 3. 두 문자열 s1, s2를 입력받은 후 
# s2의 연속부분 문자열 중 s1의 아나그램 개수를 출력하라
'''
입력
abcab aabbcbbaa
출력
2
'''
string1, string2 = input().split()
n, m = len(string1), len(string2)
cnt=0
for i in range(m-n+1):
    if sorted(string1)==sorted(string2[i:i+n]):
        cnt+=1
print(cnt)
