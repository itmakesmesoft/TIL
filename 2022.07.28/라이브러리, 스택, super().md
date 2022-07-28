# 2022.07.28

### math 라이브러리

- math.ceil(float) : 올림 함수
- math.floor(float) : 내림 함수
- math.copysign(float, int) : 두 번째 인자의 부호만 취하여 첫 번째 인자에 적용
- math.fabs(float) :  절대값을 반환
- math.factorial(int) : 팩토리얼 함수

[점프 투 파이썬](https://wikidocs.net/21116)

### random 라이브러리

- **random.random()** : 0.0~1.0 사이 실수(float)를 반환
- **random.uniform(***a, b***)** : a~b 사이의 실수(float)를 반환
- **random.randint(***a, b***)** : a~b 사이의 랜덤한 정수(int)를 반환
- **random.randrange(***[a,] ****b***)** : a~b 또는 0부터 b까지의 랜덤한 정수(int)를 반환
- **random.choice(***seq***)** : 시퀀스 타입(문자열, 튜플, 리스트)의 매개변수에서 무작위로 하나의 원소를 선택하여 반환
    
    [자세한 내용](https://blockdmask.tistory.com/383)
    

### super()

- 하위 클래스에서 부모 클래스의 속성 및 메소드를 불러올 때 사용
    
    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    		def check_age(self):
    				return True if self.age>=19 else False
    
    class Student(Person):
        def __init__(self, name, age, id):
    				# self.name = name
    				# self.age = age
    						# super().__init__()을 통해 
    					  # 부모 클래스의 속성 메소드를 불러올 수 있음.
            super().__init__(name, age)
            self.id = id
    				
    student = Student('홍길동', 20, '0021521')
    print(student.id)
    print(student.check_age())
    ```
    

### stack

- 가장 나중에 넣은 데이터를 가장 먼저 빼내는 데이터 구조. 
FILO(First In Last Out)
파이썬은 list에 이미 구현되어 있음

- **내장 함수를 이용한 스택 구현**
    - *list*.append(…) : 괄호 안의 요소를 리스트 맨 마지막에 추가
    - *list*.pop() : 맨 마지막 리스트의 요소를 꺼내고 리스트에서 삭제
    
    ```python
    a = [1,2,3,4]
    a.append(5)
    print(a) # [1,2,3,4,5]
    
    print(a.pop()) # 5
    print(a) # [1,2,3,4]
    ```
    

- **클래스를 이용한 스택 구현**
    
    ```python
    class Stack:
    		def __init__(self):
    				self.stack = []
    
    		def push(self, data):
    				self.stack.append(data)
    
    		def pop(self):
    				return self.stack.pop()
    
    		def isEmpty(self):
    				if self.stack == []:
    						return True
    				else:
    						return False
    
    		def __repr__(self):
    				return f'{self.stack}'
    
    stack1 = Stack()
    stack1.push(1)
    print(stack1) # [1]
    ```