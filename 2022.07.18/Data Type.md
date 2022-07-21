# 데이터 타입

## 변수(variable)

한 개의 데이터를 저장하기 위해 사용. 변수를 사용하면 숫자를 직접 적지 않고 의미 단위로 작성이 가능하며,  가독성이 증가, 코드 수정이 용이해짐 (추상화)

- **변수의 할당(assignment)**
변수는 할당 연산자(=)할 때에는 변수명을 적고 값을 입력해주면 됨. (*변수명 = 값)*

```python
# 변수를 할당할 때는 문자(열)와 숫자를 넣을 수 있음.
practice = '연습만이 살 길'
practice_1 = 10000000

# 같은 값은 동시에 할당도 가능
practice = practice_1 = 100

# 다른 값을 동시에 할당도 가능
practice, practice_1 = 200, 300

```
</br>

- **변수 x와 y의 값을 바꾸는 경우**

```python
# 방법 1
x, y = 10, 20
tmp = x
x = y
y = tmp
print(x, y) # 20, 10

# 방법 2 (파이썬만 가능)
x, y = 1, 2
x, y = y, x
print(x, y) # 2, 1
```

</br>

- **변수 이름 규칙**
    - 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성
    - 첫 글자에 숫자가 올 수 없음
    - 길이 제한이 없고, 대소문자를 구별
    - 내장 함수나 모듈 등의 이름 사용하지 않아야 함
    - 다음의 키워드(keywords)에서는 예약어(reserved words)로 사용할 수 없음

```python
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 
#'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
#'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
#'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

</br></br>

## 산술 연산자

기본적인 사칙 연산 및 수식 계산

| 연산자 | 내용 |
| --- | --- |
| + | 덧셈 |
| - | 빼기 |
| * | 곱셈 |
| / | 나눗셈 |
| // | 몫 |
| % | 나머지 |

</br></br>

## 문자열 자료형(String Type)

: 모든 문자는 **str**타입

- 문자열은 작은따옴표(’)나 큰따옴표(”)를 활용하여 표기
    - 문자열을 묶을 때 동일한 문장부호를 활용
    - PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함.
        
        ```python
        print('hello") # (X) 작은 따옴표와 큰 따옴표를 혼용하면 안됨
        print('hello')
        print("hello") # 한 소스코드 내에서는 하나의 문장부호로 통일 할 것.
        ```
        
    
    - 작은따옴표가 들어있거나, 큰따옴표가 들어있는 경우, 큰따옴표/혹은 작은따옴표로 문자열을 생성
        
        ```python
        print('문자열 내에서 "문자열" 생성')
        print("문자열 내에서 '문자열' 생성")
        ```
        
</br>

- 삼중 따옴표(Triple Quotes)
    
    ```python
    print('''
    여러 줄을 만드는 경우 \n
    삼중따옴표(\'\'\' 또는 \"\"\")를 이용하면 편리
    ''')
    ```
    
</br>

- Escape Sequence
    
    역슬래시(backslash)뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합
    
    | 예약 문자 | 내용(의미) |
    | --- | --- |
    | \n | 줄 바꿈 |
    | \t | 탭 |
    | \r | 캐리지 리턴 |
    | \0 | 널(Null) |
    | \\ | \ |
    | \’ | 단일인용부호(’) |
    | \“ | 이중인용부호(”) |
    
    ```python
    print('철수\'안녕\'') # 철수'안녕'
    
    print('엔터. \n 그리고 탭\t')
    #탭      , 엔터
    #내용
    ```
    
</br>

- 문자열 연산(String Concatenation)
    
    ```python
    # 덧셈
    	print('a'+'b') # ab
    
    # 곱셈
    	print('a'*3)
    ```
    
</br>

- 문자열과 변수를 함께 사용하는 법(String Interpolation)
    
    ```python
    # 1. str.format()
    	name='kim'
    	score=0.1
    	print('{}님의 점수는 {}'.format(name, score))
    	
    # 2. f-strings : python 3.6+
    	name='kim'
    	score=0.1
    	print(f'{name}님의 점수는 {score}')
    ```
    
</br></br>

## 자료형(Datatype)의 분류

- 수치형(Numeric Type)
    - **int**(정수, Integer) : 0, 100, -200과 같은 정수
        - 2진수(binary) : 0b
        - 8진수(octal) :0o
        - 16진수(hexadecimal) : 0x
    - **float**(부동소수점/실수. float point number) : 유리수와 무리수를 포함하는 실수
        - *부동 소수점*
            - 실수의 값을 처리할 때 의도하지 않은 값이 나올 수 있음
                
                ```python
                print(3.2 - 2.1) # 0.10000000000000009
                print(1.2 - 1.1) # 0.09999999999999987
                # 연산의 결과가 0.1이 아님      
                ```
                
            - 원인은 부동 소수점 때문
                - 컴퓨터는 2진수를 사용. 사람은 10진법을 사용
                - 이때 10진수 0.1은 2진수로 표현하면 0.0001100110011001100…같이 무한대로 반복
                - 무한대 숫자를 그대로 저장할 수 없어, 사람이 사용하는 10진법의 근사값을 표시
                - 0.1의 경우 3602879701896397/2**55 이며, 0.1에 가깝지만 정확이 동일하진 않음.
                - 이런 과정에서 예상치 못한 결과가 나타남(Floating point roundling error)
            - 해결책
                - 매우 작은 수보다 작은지를 확인하거나 math 모듈 활용
                
                ```python
                a = 3.2 - 3.1 # 0.10000000000000009
                b = 1.2 - 1.1 # 0.09999999999999987
                
                # 1. 임의의 작은 수 활용
                print(abs(a-b) <= 1e-10) # True
                
                # 2. python 3.5 이상
                import math
                print(math.isclose(a,b)) # True
                ```
                
    - **complex**(복소수, complex number)
- 문자열(String Type)
- 불린형(Boolean Type)
    - 논리 자료형으로, 참과 거짓을 표현하는 자료형
    - True(1) 또는 False(0) 값을 가짐
    - 비교/논리 연산에서 활용됨
- None

</br></br>

## 비교 연산자

: 수학에서 등호, 부등호와 동일한 개념. 주로 조건문에 사용되며, 값을 비교할 때 사용함.
결과는 True/False로 리턴함

| 연산자 | 내용 |
| --- | --- |
| < | 미만 |
| <= | 이하 |
| > | 초과 |
| >= | 이상 |
| == | 같음 |
| != | 같지 않음 |
| is | 객체 아이덴티티(OOP) |
| is not | 객체 아이덴티티가 아닌경우 |

```python
print(3>6)        # False
print(3.0==3)     # True
print(3>=0)       # True
print('3'!=3)     # True
print('Hi'=='Hi') # False
```
</br></br>

## 논리 연산자

- 여러 가지 조건이 있을 때
    - 모든 조건을 만족하거나(and), 여러 조건 중 하나만 만족해도 될 때(or), 특정 코드를 실행하고 싶을 때 사용.
    - 일반적으로 비교 연산자와 함께 사용
        
        
        | 연산자 | 내용 |
        | --- | --- |
        | A and B | A와 B 모두 True시 True |
        | A or B | A와 B 모두 False시 False |
        | Not | True를 False로
        False를 True로 |
        
        ```python
        print(True and True) # True
        print(True and False) # False
        print(False and True) # False 
        print(False and False) # False
        
        print(True or True) # True
        print(True or False) # True
        print(False or True) # True
        print(False or False) # False
        ```
        
    
- 주의할 점
    - Falsy : False는 아니지만 False로 취급되는 다양한 값
        - 0, 0.0, (), [], {}, None, “”(빈문자열)
    - 논리 연산자도 우선순위가 존재
        - not, and, or 순으로 우선순위가 높음 ⇒ 소괄호로 묶으면 우선
        
- 논리 연산자의 단축 평가
    
    ```python
    # and연산에서 첫번째 값이 False인 경우 무조건 False ⇒ 첫번째 값 반환
    print(3 and 5) # 5
    print(3 and 0) # 0
    print(0 and 3) # 0
    print(0 and 0) # 0
    # 0은 False, 1은 True
    
    # 결과가 확실한 경우 두번째 값은 확인하지 않고 첫번째 값 반환
    print(5 or 3) # 5
    print(3 or 0) # 3
    print(0 or 3) # 3
    print(0 or 0) # 0
    
    # or연산에서 첫번째 값이 True인 경우 무조건 True ⇒ 첫번째 값 반환
    a = 5 and 4
    print(a)      # 4
    b = 5 or 3
    print(b)      # 5
    c = 0 and 5
    print(c)      # 0
    d = 5 or 0
    print(d)      # 5
    ```
    
</br></br>

## 컨테이너

: 여러 개의 값(데이터)을 담을 수 있는 것(객체)으로, 
서로 다른 자료형을 저장할 수 있음 (파이썬만의 특징)

- 컨테이너의 분류
순서가 있는 데이터(Ordered) vs 순서가 없는 데이터(Unordered)
*”순서가 있다” ≠ “정렬되어 있다.”*
- 시퀀스형(순서 있음)
    - 리스트(가변형; mutable)
    - 튜플(불변형; immutable)
    - 레인지(불변형; immutable)
- 비시퀀스형(순서 없음)
    - 세트(가변형; mutable)
    - 딕셔너리(가변형; mutable)

</br></br>

## 리스트(List)

: 여러 개의 데이터를 순서가 있는 구조로 저장하고 싶을 때 사용. 
요소를 추가하거나 삭제, 편집이 가능(mutable)

- 리스트 생성
리스트명을 적고 아래와 같이 list() 또는 대괄호[]를 이용해 생성.
    
    ```python
    Array = list()
    Array_1 = []
    print(type(Array))   # <class 'list'>
    print(type(Array_1)) # <class 'list'>
    ```
    
</br>

- 값에 대한 접근
리스트는 순서가 있는 시퀀스로, 인덱스(0~n-1)를 통해 접근 가능
    
    ```python
    li=[1,2,3,4,5]
    print(li[0])     # 1
    print(li[1])     # 2
    print(li[5])     # 4
    ```
    
</br>

- 리스트 요소 추가/변경
list.append(”내용”)를 이용해 요소를 추가하거나 인덱스에 접근하여 추가 또는 변경 가능.
    
    ```python
    Array=['과자', '빵']
    Array.append('아이스크림')
    Array[3]='사과'
    print(Array[2])   # '아이스크림'
    Array[0]='수박'
    print(Array)      # ['수박', '빵', '아이스크림', '사과']
    ```
    
</br></br>

## 튜플(Tuple)

: 리스트와 비슷하지만 한 번 선언 시 값을 수정을 할 수 없음. (불변형)

- 튜플 생성
튜플은 소괄호()에 값을 넣어 선언할 수 있음. *(리스트의 경우 대괄호[])*
    
    ```python
    tuple1 = (1, 2, 3)    # 튜플 선언됨
    print(tuple(3, 4, 5)) # (3, 4, 5)
    tuple1[1]=2           # TypeError : 'tuple' object does not support item assignment
    									    # 튜플은 수정이 불가능하기 때문에 오류 방생
    ```
    
</br>

- 튜플 생성 시 주의사항
    - 단일 항목의 경우
        - 하나의 항목으로 구성된 튜플은 생성 시 값 뒤에 쉼표를 붙여야 함
    - 복수 항목의 경우
        - 마지막 항목에 붙은 쉼표는 없어도 되지만, 넣는 것을 권장(Trailing comma)
    
    ```python
    tuple_a = (1,)
    print(tuple_a) # (1,)
    print(type(tuple_a)) #<class 'tuple'>
    
    tuple_b = (1, 2, 3,)
    print(tuple_b) # (1, 2, 3)
    print(type(tuple_b)) #<class 'tuple'>
    ```
    
    ```python
    a = 1,
    print(a) # (1,)
    print(type(a)) # <class 'tuple'>
    
    b = 1, 2, 3
    print(b) # (1, 2, 3)
    print(type(b)) #<class 'tuple'>
    ```
    </br>

- 튜플 대입
: 우변의 값을 좌변의 변수에 한 번에 할당하는 과정
튜플은 일반적으로 파이썬 내부에서 활용되며, 추후 함수에서 복수의 값을 반환할 때에도 활용
    
    ```python
    x, y = 1, 2
    print(x, y) # 1, 2
    
    #실제로 튜플로 처리
    x, y = (1, 2)
    print(x, y) # 1, 2
    ```
    
</br></br>

## Range

숫자의 시퀀슬르 나타내기 위해 사용하며, 주로 반복문과 함께 사용됨

```python
# 기본형 : range(n) => 0 ~ n-1까지
print(list(range(4))) # [0, 1, 2, 3]

# 범위 지정 : range(n, m) => n ~ m-1까지
print(list(range(1,6))) # [1, 2, 3, 4, 5]

# 스텝 지정 : range(n, m, s) => n ~ m-1까지 s만큼 증가
print(list(range(1,6,2)))  # [1, 3, 5]
print(list(range(6,1,-1))) # [6, 5, 4, 3, 2]
print(list(range(6,1,-2))) # [6, 4, 2]
```

</br></br>

## 슬라이싱 연산자

: 시퀀스의 인덱스와 콜론을 사용하여 문자열의 특정 부분만 잘라내는게 가능
슬라이싱을 이용하여 문자열을 나타낼 때 콜론을 기준으로 앞 인덱스에 해당하는 문자는 포함되지만 뒤 인덱스에 해당 문자는 미포함

```python
# 리스트[1:4]에서 1은 포함, 4는 미포함
print([1, 2, 3, 5][1:4]) # [2, 3, 5]

# 튜플
print((1, 2, 3)[:2]) # (1, 2)

# range
print(range(10)[5:8]) # range(5, 8)

# 문자열
print('abcd'[2:4]) # cd

# 스텝 지정
print([1, 2, 3, 5][0:4:2]) # [1, 3]
print((1, 2, 3, 5)[0:4:2]) # (1, 3)
print(range(10)[1:5:2]) # range(1, 5, 2)
print('abcded'[1:4:2]) # bd

# 생략
print([1, 2, 3, 4, 5][::2]) # [1, 3, 5]
print([1, 2, 3, 4, 5][2:])  # [3, 4, 5]
```
</br></br>

## Set(세트)

- Set이란 중복되는 요소가 없이, 순서에 상관없는 데이터들의 묶음
    - 데이터의 중복을 허용하지 않기 때문에 중복되는 원소가 있다면 하나만 저장
    - 순서가 없기 때문에 인덱스를 이용한 접근 불가능
    - 수학에서의 집합을 표현한 컨테이너
        - 집합 연산이 가능(여집합을 표현하는 연산자는 별도로 존재하진 않음)
        - 중복된 값이 존재하지 않음
    - 담고 있는 요소를 삽입, 변경, 삭제 가능 ⇒ 가변 자료형(mutable)

</br>

- Set의 생성
    
    ```python
    # 중괄호{} 또는 set()을 통해 생성. 빈 셋을 만들기 위해서는 반드시 set() 사용
    print({1, 2, 3, 4})       #{1, 2, 3, 4}
    print(type({1, 2, 3, 4})) # <class 'set'>
    
    # 빈 중괄호는 Dictionary
    blank = {}
    print(type(blank))     # <class 'dict'>
    blank_set = set()
    print(type(blank_set)) # <class 'set'> 
    
    #set은 순서가 없는 비시퀀스형으로, 인덱스 접근 불가
    print({1, 2, 3}[0]) # TypeError: 'set' object is no subscriptable
    ```
    
</br>

- set 사용하기
    
    ```python
    # 요소 개수
    my_list = ['가', '나', '다', '가', '나']
    print(len(set(my_list))) # 3
    # my_list를 set로 변환 후 개수를 셈
    # set을 사용하는 순간 중복 요소는 제거됨
    ```
    
</br>

- set 연산자
    
    
    ```python
    a_set = {1, 2, 3, 4}
    b_set = {1, 2, 3, 'hello', (1,2,3)}
    
    print(a_set | b_set) # {1,2,3,4, (1,2,3), 'hello'}
    print(a_set & b_set) # {1, 2, 3}
    print(a_set - b_set) # {(1,2,3), 'hello'}
    print(a_set ^ b_set) # {'hello', 4, (1,2,3)}
    ```
    
    | 연산자 | 기호 |
    | --- | --- |
    | 합집합 | | |
    | 교집합 | & |
    | 차집합 | - |
    | 대칭차집합 | ^ |
    | (여집합은 없음) |  |

</br></br>

## 딕셔너리(Dictionary)

: 사전형 데이터를 의미하며, key와 value를 가짐.

- 3.7부터는 ordered(순서 있음), 이하 버전은 unordered(순서 없음)
    - Dictionary의 키(key)
        - key는 변경 불가능한 데이터(immutable)만 활용 가능
        - string, integer, float, boolean, tuple, range
    - 각 키(key)의 값(values)
        - 어떠한 형태든 관계없음
- 딕셔너리의 생성
    - 딕셔너리는 중괄호({ }) 또는 dict()를 통해 생성
    - key를 통해 value에 접근
    
    ```python
    dict_a = {]
    print(type(dict_a)) # <class 'dict'>
    
    dict_b = dict()
    print(type(dict_b)) # <class 'dict'>
    
    dict_a = {'a':'apple', 'b':'banana', 'list':[1, 2, 3]}
    print(dict_a['a'])  # 'apple'
    
    dict_b = {a:'apple', b:'banana', list:[1, 2, 3]}
    print(dict_b)       # {'a':'apple', 'b':'banana', 'list':[1, 2, 3]}
    ```
    
</br></br>

## 형 변환(TypeCasting)

- 파이썬에서 데이터 형태는 서로 변환할 수 있음
- 암시적 형 변환(impicit) ⇒ 자동
    - 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환하는 경우
    
    ```python
    # 1. bool type
    print(True + 3) # 4
    
    # 2. Numeric type (int, float)
    print(3 + 5.0)  # 8.0
    ```
    </br>
    

- 명시적 형 변환(Explicit) ⇒ 의도
    - 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환하는 경우
    - int
        - str, float ⇒ int
        - 단, 형식에 맞는 문자열만 정수로 변환 가능
    
    ```python
    # 문자열은 암시적 타입 변환이 되지 않음
    	print('3'+ 4) # TypeError : can only concatenate str (not "int") to str
    
    # 명시적 타입 변환이 필요
      print(int('3') + 4) # 7
    
    # 정수 형식이 아닌 경우 타입 변환할 수 없음
      print(int('3.5') + 4) # ValueError : invalid literal for int() with base 10:
    ```
    </br>

    - float
        - str(참고), int ⇒ float
        - 단, 형식에 맞는 문자열만 float로 변환 가능
    
    ```python
    print('3.5'+3.5)  # TypeError : can only concatenate str (not "float") to str
    
    # 정수 형식인 경우에도 float로 타입 변환
    print(float('3')) # 3.0
    
    # float 형식이 아닌 경우 타입 변환할 수 없음
    print(float('3/4') + 5.3) # ValueError : could not convert string to float:
    ```
    
    </br>

    - str
        - int, float, list, tuple, dict ⇒ str
    
    ```python
    print(str(1))          # '1'
    print(str(1.0))        # '1.0'
    print(str([1, 2, 3]))  # '[1, 2, 3]'
    print(str({1, 2, 3}))  # '{1, 2, 3}'
    ```
    
</br>

## 컨테이너 형 변환
|  | string | list | tuple | range | set | dictionary |
| --- | --- | --- | --- | --- | --- | --- |
| string |  | O | O | X | O | X |
| list | O |  |  | X | O | X |
| tuple | O | O |  | X | O | X |
| range | O | O | O |  | O | X |
| set | O | O | O | X |  | X |
| dictionary | O | O (key만) | O (key만)  | X | O (key만)  |  |