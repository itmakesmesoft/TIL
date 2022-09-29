# 해쉬 자료구조 : 빠른 검색속도

# 빠른 검색을 위한 자료구조 : BST(logn), HASH(O(1))

# 파이썬에서는 딕셔너리를 활용




# burger={'cy':3000,'wp':5000}

# # 싸이버거 가격만 출력!
# print(burger['cy'])

# burger={
#     'mst':{'cy':3000,'chips':500},
#     'mc':{'bm':5000,'chips':700}
# }

# # 빅맥 가격만 출력!
# print(burger['mc']['bm'])

# # 맘스터치 칩스 가격 1000원 인상
# burger['mst']['chips']+=1000
# print(burger['mst']['chips'])

# # print(burger['mst']['coke']) # 키 에러 발생
# print(burger['mst'].get('coke', 'none')) # 키 에러 발생 방지

# # 딕셔너리 mst 값 삭제
# # del burger['mst'] # 키가 없는 경우 에러 발생
# # print(burger)
# # ret = burger.pop('ㄴㅇㄱ', '없음') # 키가 없어도 에러 발생하지 않음
# # print(ret)


# #연습문제
# #딕셔너리 키, 값 출력하기
# # burger={
# #     'mst':{'cy':3000,'chips':500},
# #     'mc':{'bm':5000,'chips':700}
# # }

# # 출력결과 1
# # mst bm
# # keys = list(burger.keys())
# # keys2 = list(burger[keys[1]].keys())
# # print(keys[0])
# # print(keys2[0])


# # print(burger['mc']['bm'])


# # 출력결과 2
# # for val in burger.values():
# #     print(val)
# # {'cy':3000,'chips':500}
# # {'bm':5000,'chips':700}


# # 출력결과 3
# # for val in burger.values():
# #     for j in val.values():
# #         print(j)

# # 3000
# # 500
# # 5000
# # 700


# # 출력결과 4
# # mst {'cy': 3000, 'chips': 500}
# # mc {'bm': 5000, 'chips': 700}

# # for key, val in burger.items():
# #     print(key, val)


# # 출력결과 5
# # cy 3000
# # chips 500
# # bm 5000
# # chips 700

# # for key in burger.keys():
# #     for k, v in burger[key].items():
# #         print(k, v)




# # =============================================

# # 정렬 후 출력하기

# mst={'cy':3000,'chips':500,'coke':300}

# # 가격 오름차순 으로 정렬 후 출력하기
# # 출력결과
# # coke 300
# # chips 500
# # cy 3000
# sorted_mst = sorted(mst.items(), key=lambda x:x[1])
# for k, v in sorted_mst:
#     print(k, v)

# # 가격 내림차순 으로 정렬 후 출력하기
# #출력결과
# # cy 3000
# # chips 500
# # coke 300
# sorted_mst = sorted(mst.items(), key=lambda x:x[1], reverse=True)
# for k, v in sorted_mst:
#     print(k, v)

# # 이름 기준으로 오름차순
# # 출력결과
# # chips 500
# # coke 300
# # cy 3000
# sorted_mst = sorted(mst.items(), key=lambda x:x[0])
# for k, v in sorted_mst:
#     print(k, v)


# # 이름 기준으로 내림차순
# # 출력결과
# # cy 3000
# # coke 300
# # chips 500
# sorted_mst = sorted(mst.items(), key=lambda x:x[0], reverse=True)
# for k, v in sorted_mst:
#     print(k, v)


# fastfood=[
#     {'name':'mst','burger':3000,'chips':500,'tasty':'C'},
#     {'name':'mc','burger':5000,'chips':700,'tasty':'A'},
#     {'name':'bk','burger':7000,'chips':300,'tasty':'A'},
# ]
# # sorted_resonable = sorted(fastfood, key=lambda x:-x['burger'])
# # sorted_taste = sorted(sorted_resonable, key=lambda x:x['tasty'])

# ret = sorted(fastfood, key=lambda x:(x['tasty'], -x['burger'])) # -x['burger'] => '-'를 곱해서 음수로 처리=> reverse로 정렬됨
# print(ret)










# Counter 모듈 => 해쉬 기반으로 DAT 구현
from collections import Counter

a = [1,1,1,1,2,3,4]
b = [1,1,2,3]

print(Counter(a))
print(Counter(b))
print(Counter(a)-Counter(b))
c = Counter(a)-Counter(b)
print(list(c.items())[0][1])