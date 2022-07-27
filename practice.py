# def function(param):
#     res=""
#     cnt=0 # 가장 첫번째 대문자는 바꾸지 않기 위해 카운트 변수 설정
#     for p in param:
#         if p.isalpha():
#             if p.isupper() and cnt==0: # 문자가 대문자이고, cnt가 0인 경우
#                 res+=p #그대로 대문자를 출력하고
#                 cnt=1  #cnt=1로 대입
#             else:
#                 res+=p.lower()
#         else:
#             if p in [',','.','\'']:
#                 res+=p
#     return res

# print(function(input()))



# def sum_of_repeat_number(param):
#     res=[]
#     for p in param:
#         if param.count(p)==1:
#             res.append(p)
#     return sum(res)


# arr=list(map(int, input().split())) #입력 예시 3 4 5 23 3 4
# print(sum_of_repeat_number(arr))




# words_dict = {'proper' : '적절한',
# 'possible' : '가능한',
# 'moral' : '도덕적인',
# 'patient' : '참을성 있는',
# 'balance' : '균형',
# 'perfect' : '완벽한',
# 'logical' : '논리적인',
# 'legal' : '합법적인',
# 'relevant' : '관련 있는',
# 'responsible' : '책임감 있는',
# 'regular' : '규칙적인'}


# def function(param):
#     res=[]
#     for word in param:
#         if word[0] in ['b','m','p']:
#             res.append('im'+word)
#         elif word[0] == 'l':
#             res.append('il'+word)
#         elif word[0] == 'r':
#             res.append('ir'+word)
#         else:
#             res.append('in'+word)
#     res.sort()
#     return res

# print(function(words_dict))

# 1.
def count_vowels(param):
    count=0
    for vowel in ['a','e','i','o','u']:
        count+=param.count(vowel)
    return count
word=input()
print(count_vowels(word))

# 2.
answer : (4)

# 3. 
def only_square_area(widths, heights):
    res=[]
    for i in widths:
        if i in heights:
            res.append(i**2)
    return res
widths=[32,55,63]
heights=[13,32,40,55]
print(only_square_area(widths, heights))