# 객체 지향 프로그래밍(OOP)

## 객체 지향 프로그래밍(OOP; Object-Oriented Programming)

- 프로그램을 여러 개의 독립된 객체들과 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법.
- EX) 콘서트(가수 객체, 감독 객체, 관객 객체)

### 객체지향 프로그래밍이 필요한 이유

- 현실 세계를 프로그램 설계에 반영(추상화)

### 객체지향의 핵심 4가지

- **추상화**
    - 복잡한 것은 숨기고, 필요한 것만 들어내는 것
        - ‘홍길동’, ’김철민’ ⇒ 사람
        - 앞으로 걷기, 뛰기 ⇒ 움직임
- **상속**
    - 두 클래스 사이 부모-자식 관계를 정립하는 것
    - 클래스는 상속이 가능함
    - `class ChildClass(ParantClass):`
    - 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약조건을 모두 상속받음
    - 부모 클래스의 속성, 메서드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐
    - 두 클래스 사이에 공통부분을 뽑아 부모 클래스를 만들고 하위클래스에서 상속받으면 메서드를 재사용할 수 있음.
    - **상속 관련 메서드**
        - **isinstance(***object, classinfo***)**
            
            classinfo의 instance이거나 subclass인 경우 **True**
            
        - **issubclass(***class, classinfo***)**
            
            class가 classinfo의 subclass면 **True**
            
        - **super()**
            
            자식클래스에서 부모클래스를 사용하고 싶은 경우
            
        - 
    - 다중상속
        - 두 개 이상의 클래스를 상속 받는 경우
        - 상속받은 모든 클래스의 요소를 활용 가능함
        - 중복된 속성이나 메선드가 있는 경우 상속 순서에 의해 결정
        - **mro 메서드(Method Resolution Order)**
            - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
            - 기존의 인스턴스 → 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 → 자식 클래스 → 부모 클래스로 확장
            
            ```python
            print(FirstChild.mro())
            '''
            [<class '__main__.FirstChild'>, <class '__main__.Dad'>, 
            <class '__main__.Mom'>, <class '__main__.Person'>,<class 'object'>]
            '''
            ```
            

- **다형성(Polymorphism)**
    - 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미
    - 즉, 서로 다른 클래스에 속해있는 객체들이 동일한 메세지에 대해 다른 방식으로 응답할 수 있음
    - 메서드 오버라이딩
        - 상속받은 메서드를 재정의
            - 클래스 상속 시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경
            - 부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용
            - 부모 클래스의 메서드를 실행시키고 싶은 경우 super를 활용
            
- **캡슐화**
    - 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 엑세스를 차단
        - ex) 주민등록번호
    - 파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음
    - 접근 제어자 종류
        - Public Access Modifier
        - Protected Access Modifier
        - Private Access Modifier
    - Public Member
        - 언더바 없이 시작하는 메서드나 속성
        - 어디서나 호출이 가능, 하위 클래스 override 허용
        - 일반적으로 작성되는 메서드와 속성의 대다수 차지
    - Protected Member
        - 언더바 1개로 시작하는 메서드나 속성
        - 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능(오류가 발생하진 않음)
        - 하위 클래스 override 허용
    - Private Member
        - 언더바 2개로 시작하는 메서드나 속성
        - 본 클래스 내부에서만 사용이 가능
        - 하위클래스 상속 및 호출 불가능(오류)
        - 외부 호출 불가능(오류)
    - getter 메서드와 setter 메서드
        - 변수에 접근할 수 있는 메서드를 별도로 생성
            - getter 메서드 : 변수의 값을 읽는 메서드
                - @property 데코레이터 사용
            - settet 메서드 : 변수의 값을 설정하는 성격의 메서드
                - @변수.setter 사용

### 객체지향의 장/단점

- **장점**
    - 클래스 단위로 모듈화시켜 개발할 수 있으므로 많은 인원이 참여하는 대규모 소프트웨어 개발에 적합
    - 필요한 부분만 수정하기 쉽기 때문에 프로그램 유지보수가 쉬움
    
- **단점**
    - 설계 시 많은 노력과 시간이 필요함
        - 다양한 객체들의 상호 작용 구조를 만들기 위해 많은 시간과 노력이 필요
    - 실행 속도가 상대적으로 느림
        - 절차 지향 프로그래밍이 컴퓨터의 처리구조와 비슷해서 실행 속도가 빠름

### 객체와 인스턴스

- 객체는 속성(변수)과 행동(함수-메서드)으로 구성된 모든 것.
- 인스턴스는 클래스로 만든 객체를 의미
- 객체(obejct)는 특정 타입의 인스턴스(instance)임.
    - 123은 int의 인스턴스
    - ‘hello’는 str의 인스턴스
    - [1,2,3]은 list의 인스턴스

### 객체의 특징

- 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
- 속성(attribute) : 어떤 상태(데이터)를 가지는가?
- 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

### 기본문법

```python
class Myclass: # 클래스 정의
    pass

my_instance = Myclass() # 인스턴스 생성

my_instance.my_method() # 매서드 호출

my_instance.my_attribute # 속성
```

### 객체 비교하기

- `==`
    - 동등한(equal)
    - 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
    - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키는 것은 아닐 수도 있음.
- `is`
    - 동일한(identical)
    - 두 변수가 동일한 객체를 가리키는 경우 True

```python
a=[1,2,3]
b=[1,2,3]
print(a==b, a is b) # True False

a=[1,2,3]
b=a
print(a==b, a is b) # True True
```

### 속성

- 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미
- 클래스 변수/ 인스턴스 변수가 존재
- **클래스 변수**
    - 클래스 선언 내부에서 정의
    - <classname>.<name>으로 접근 및 할당
    - 클래스 변수를 변경할 때는 **클래스.클래스변수** 형식으로 변경
- **인스턴스 변수**
    - 인스턴스가 가지고 있는 고유의 속성(attribute)
    - **생성자( `__init__` ) 메서드**에서 self.<name>으로 정의
    - 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당

```python
class Person:
		count=0
		blood_type = 'A' # 클래스 변수 정의
		population = 100
		def  __init__(self, name): # 인스턴스 변수 정의
				self.name = name
				Person.count+=1

person1 = Person('지민') # 인스턴스 변수 할당
person2 = Person('지연')
print(person1.blood_type) # 'A' <= 클래스 변수 접근
print(person1.name) # '지민' <= 인스턴스 변수 접근
print(Person.count) # 2

# 클래스 변수 변경
Person.blood_type = 'B' 클래스 변수를 변경하면
print(Person.blood_type) # B
print(person1.blood_type) # B 해당 클래스의 인스턴스가 모두 변경 
print(person2.blood_type) # B

person1.blood_type = 'O' # 만약 인스턴스를 통해 클래스변수를 변경 시
print(Person.blood_type) # B
print(person1.blood_type) # A 해당 인스턴스만 변경되고 
print(person2.blood_type) # B 해당 클래스의 다른 인스턴스는 변경되지 않음

```

### OOP 메서드(Object-Oriented Programming)

- 특정 데이터 타입/클래스의 객체 에 공통적으로 적용 가능한 행위(함수)

```python
class Person:
		def __init__(self.name):
				self.name=name

		def eat(self, food):
				print(f'{food} 냠냠')

person1=Person('홍길동')
person1.eat('피자') # 피자 냠냠
```

- **메서드 종류**
    - **인스턴스 메서드**
        - 호출한 인스턴스를 의미하는 self 매개 변수를 통해 인스턴스를 조작
        
        ```python
        class MyClass:
        		def instance_method(self):
        				return 'instance method', self
        
        my_instance = MyClass()
        print(my_instance.instance_method()) 
        # ('instance method', <__main__.MyClass at 0x184fd086a00>)
        ```
        
        - `self`
            - 인스턴스 자기 자신
            - 파이썬에서 인스턴스 메서드는 호출 시 첫번째 인자로 인스턴스 자신(self)이 전달되게 설계됨
        - `__init__` (생성자 메서드)
            - 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
            - 인스턴스 변수들의 초기값을 설정
        - `__del__` (소멸자 메서드; destructor)
            - 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메서드
        - **매직 메서드( __ )**
            - Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드로, 스페셜 메서드 혹은 매직 메서드라고 불림
            - 특정 상황에서 자동으로 불리는 메서드
            - ex)
                - `__str__(self)` : 해당 객체의 출력 형태를 지정
                    - 프린트 함수를 호출할 때, 자동으로 호출
                    - 어떤 인스턴스를 출력하면 `__str__`의 return값이 출력
                - `__len(self)__`, `__repr__(self)` 등
                
                ---
                
    
    - **클래스 메서드**
        - 클래스가 사용할 메서드
        - @classmethod 데코레이터를 사용하여 정의
        - 클래스를 의미하는 cls 매개 변수를 통해 클래스를 조작
        
        ```python
        class MyClass:
        		@classmethod
        		def class_method(cls):
        				return 'class method', cls
        
        MyClass.class_method()
        ```
        
    
    - **데코레이터**
        - 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
        - @데코레이터(함수명) 형태로 함수 위에 작성
        - 순서대로 적용되기 때문에 작성 순서가 중요
        
        ```python
        # 데코레이터가 없는 경우
        def hello():
            print("hello")
        
        def add_print(original): # 파라미터로 함수를 받는다
        		def wrapper(): # 함수 내에서 새로운 함수 선언
        				print("함수 시작") # 부가기능 -> original 함수를 꾸밈
        				original() 
        				print("함수 끝") # 부가기능 -> original 함수를 꾸밈
        		return wrapper # 함수를 return
        
        print_hello = add_print(hello)
        print_hello()
        
        # 데코레이터 이용
        def add_print(original): # 파라미터로 함수를 받는다
        		def wrapper(): # 함수 내에서 새로운 함수 선언
        				print("함수 시작") # 부가기능 -> original 함수를 꾸밈
        				original() 
        				print("함수 끝") # 부가기능 -> original 함수를 꾸밈
        		return wrapper # 함수를 return
        
        @add_print # add_print를 사용해서 print_hello()함수를 꾸며주도록 하는 명령어
        def print_hello():
        		print('hello')
        
        print_hello()
        ```
        
    
    - **정적 메서드(Static Method)**
        - 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메서드
        - 속성을 다루지 않고 단지 기능(행동)만을 하는 메서드를 정의할 때 사용
        - 즉, 객체 상태나 클래스 상태를 수정할 수 없음
        - @staticmethod 데코레이터를 사용하여 정의
        - 일반 함수처럼 동작하지만, 클래스의 이름 공간에 귀속됨.
            - 주로 해당 클래스로 한정하는 용도로 사용
        
        ```python
        class MyClass:
        		@staticmethod
        		def static_method(arg1, ...):
        
        MyClass.static_method(...)
        ```
        
    
    - **인스턴스와 클래스 간의 이름 공간(namespace)**
        - 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
        - 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
        - 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색
        
        ```python
        # Person 정의
        class Person:
        		name= 'Unknown'
        		def talk(self):
        				print(self.name)
        
        p1 = Person()
        p1.talk() # Unknown
        
        # p2 인스턴스 변수 설정 전/후
        p2 = Person()
        p2.talk() # Unknown
        p2.name = '홍길동'
        p2.talk() # 홍길동
        
        print(Person.name)
        print(p1.name) # unknown <= 클래스 변수
        print(p2.name) # 홍길동 <= 인스턴스 변수
        ```