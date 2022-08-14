# JAVA

### Java

- 자바는 컴파일 언어로, 
java 파일을 컴퓨터가 이해할 수 있는 class 파일(byte code)로 컴파일 해야 함
- 컴파일 시 bin폴더 안에 class 파일이 저장됨(숨김 폴더)
- `javac` : java파일을 class파일로 컴파일하는 CLI 명령어
- `java (클래스이름)` : 클래스 실행 명령어

## main method

- 실행 명령인 `java`를 실행 시 가장 먼저 호출되는 부분
- 만약, Application에서 main()메소드가 없다면 실행되지 않음
- Application의 시작
    
    ```java
    public class ClassName {
    		public static void main(String[] args) {
    				// 기본 형태
    		}
    }
    ```
    

### 주석

```java
**//** : 한 줄 주석처리
**/* 내용 */** : 여러 줄 주석처리
**/**** 
* Documentation API를 위한 주석
***/**
```

### 출력

- **print : 줄바꿈 없이 출력**
- **println : 출력 후 줄바꿈**
- **printf : 여러 타입의 값을 한꺼번에 출력할 때 사용**
    - `%d` : 정수
    - `%f` : 실수
    - `%c` : 문자
    - `%s` : 문자열
    
    ```java
    package javaPractice;
    public class practice {
    	public static void main(String[] args) {
    		// 정수(10진수)
    		System.out.printf("%d \n", 10); // 10
    		// 정수(8진수)
    		System.out.printf("%o \n", 10); // 12
    		// 정수(16진수)
    		System.out.printf("%X \n", 10); // A
    		// 정수(16진수)
    		System.out.printf("%x \n", 10); // a
    		
    		// 4칸 확보한 뒤 오른쪽부터 차지
    		System.out.printf("%4d \n", 10); //    10
    		// 4칸 확보한 뒤 왼쪽부터 차지
    		System.out.printf("%-4d \n", 10); // 10   
    		// 4칸 확보한 뒤 오른쪽부터 차지하고 빈칸 0채움
    		System.out.printf("%04d \n", 10); // 0010
    		
    		// 실수
    		System.out.printf("%f \n", 10.1);
    		// 실수(소숫점 둘째자리까지)
    		System.out.printf("%.2f \n", 10.1);
    
    		// 문자열 - 문자열은 반드시 쌍따옴표(") 사용
    		System.out.printf("%s \n", "홍길동");
    		// 문자 - 문자는 반드시 따옴표(') 사용
    		System.out.printf("%c \n", 'ㅎ');
    		
    		// 여러 타입 동시에 출력
    		System.out.printf("안녕하세요 저는 %s입니다. 제 나이는 %d살 입니다.", "홍길동", 100);
    		// 안녕하세요 저는 홍길동입니다. 제 나이는 100살 입니다.
    	}
    }
    ```
    

### 복제(Copy)와 참조(Reference)

- JAVA에는 원시 타입(Primitive Type)과 참조 타입(Reference Type)이 존재
- **원시 타입(Primitive Type)**
    - java의 메모리 구조 중 Stack 영역에 직접 값을 저장
        
        
        | 종류 | 데이터형 | 크기 | 표현 범위 |
        | --- | --- | --- | --- |
        | 논리형 | boolean | 1 byte (8 bit) | true / false |
        | 문자형 | char | 2 byte (16 bit) | '\u0000' ~ 'uFFFF' (16비트 유니코드 문자 데이터) |
        | 정수형 | byte | 1 byte (8 bit) | 128 ~ 127 |
        |  | short | 2 byte (16 bit) | -32768 ~ 32767 |
        |  | int | 4 byte (32 bit) | 2147483648 ~ 2147483647( -21억 ~ + 21억) |
        |  | long | 8 byte (64 bit) | -9223372036854775808 ~ 9223372036854775807(-100경 ~ + 100경) |
        | 실수형 | float | 4 byte (32 bit) | 1.4E-45 ~ 3.4028235E38 |
        |  | double | 8 byte (64 bit) | 4.9E-324 ~ 1.7976931348623157E308 |
- **참조 타입(Reference Type)**
    - java의 메모리 구조 중 Heap 영역에 실제 값을 저장하고 Heap 영역의 주소(참조 값)를 Stack 영역에 저장
    - 문자열, 배열, 열거형 상수, 클래스, 인터페이스 등
    - 최소 2번 메모리 접근이 필요하기 때문에 원시 타입에 비해 상대적으로 접근 속도가 느린 편
    - 원시타입보다 참조타입이 사용하는 메모리 양이 압도적으로 높음. 일반적으로64bits 차지
    - 원시 타입은 null을 담을 수 없지만, 참조타입은 null을 담을 수 있음
    원시타입의 경우 값이 없으면 디폴트 값을 반환함 (int→0, boolean→false)
    - 원시 타입은 제네릭 타입에서 사용할 수 없지만, 참조 타입은 가능
        
        [원시타입, 참조타입(Primitive Type, Reference Type)](https://velog.io/@gillog/%EC%9B%90%EC%8B%9C%ED%83%80%EC%9E%85-%EC%B0%B8%EC%A1%B0%ED%83%80%EC%9E%85Primitive-Type-Reference-Type)
        

## **연산자**

- **최우선 연산자** : (), .참조연산자 [] 배열 참조 연산자
- **단항 연산자**
    - 증감 연산자 ++, -- : 피연산자의 값을 1증가 또는 감소 시킨다
        - 전위형(prefix) ++i
        - 후위형(postfix) i--
    - 부호 연산자  +,- : 숫자의 부호
    - 논리 부정 연산자 ! : 논리값을 반전
    - 비트 부정 연산자 ~ : 비트 값을 반전
    - 형 변환 연산자 (type)
- **산술 연산자** (정수와 실수의 연산 → 실수로 반환)
    - 곱하기 : *
    - 나누기 : /
    - 나머지 : %
    - 더하기 : +
    - 뺴기 : -
- **비교 연산자**
    - 대소 비교 연산 : >, >= <, <=
    - 동등 비교 연산 : ==, != (* String 비교 시 equals()를 사용해야 함)
    - 객체 타입 비교 연산
- **논리 연산자**
    - && : 논리곱 (AND) 피연산자가 모두 true인 경우 true
    - || : 논리합 (OR) 피연산자 중 하나라도 true인 경우 true
    - ! : 논리 부정(NOT) 피연산자의 결과를 반대로 반환
- **삼항 연산자**
    - 조건식 ? 식1 : 식2
    - 조건식이 true인 경우 식1 수행
    - 조건식이 false인 경우 식2 수행
- **복합 대입 연산자**
    - +=, -=, *=, /=
    ex) i+=1 ⇒ i=i+1

## 제어문(조건문)

- **if 문 / if - else 문 / if - else if - else 문**
    - 조건식의 결과에 따라 블록 실행 여부가 결정
    - 조건식 : true/ false 값을 산출할 수 있는 연산식 또는 boolean 타입 변수가 올 수 있음
        
        ```java
        public class practice {
        		public static void main(String[] args) {
        				int age = 15;
        				if(age >= 20){
        					System.out.println("성인");
        				} else if(age >= 14) {
        					System.out.println("청소년");
        				}
        				 else{
        					System.out.println("어린이");
        				}
        		}
        }
        ```
        

- **switch 문**
    - 인자로 선택변수를 받아 변수의 값에 따라서 실행문이 결정
    - default는 else와 같은 역할
        
        ```java
        public class practice {
        		public static void main(String[] args) {
        				int month = 12;
        				switch(month) {
        						// 아래와 같이 다른 케이스에 같은 결과값을 출력하고 싶은 경우, 생략 가능
        						case 1:
        						case 3:
        						case 5:
        						case 7:
        						case 8:
        						case 10:
        						case 12:
        								System.out.println("31일");
        								break;
        						case 4:
        						case 6:
        						case 9:
        						case 11:
        								//윤년 판별 필요
        								System.out.println("28일");
        								break;
        						default:
        								System.out.println("존재하지 않음");
        				}
        		}
        }
        ```
        
    

## 제어문(반복문)

- **for 문**
    
    ```java
    for(초기화식; 조건식; 증감식) { 
    		//초기화식, 증감식은 컴마(,)를 이용하여 둘 이상 작성 가능
    		//반복 수행할 문장
    }
    ```
    
    - 초기화는 반복문이 시작될 때 한 번 실행됨
    - 조건식이 false이면 반목문 종료
    - 증감식은 반복문의 반복이 끝나면 실행
    - 초기화식, 증감식은 (,)을 이용하여 둘 이상을 작성할 수 있음
    - 필요하지 않은 부분은 생략 가능. 
    ex) `for( ; ; )` : 무한 루프
        
        ```java
        public class practice {
        		public static void main(String[] args) {
        				for(int i = 0, j = 10; i<10; i++, j--) {
        						//반복 수행할 문장
        				}
        		}
        }
        ```
        
    
- **while 문**
    
    ```java
    while (조건식) { 
    		//조건식이 참인 경우에만 반복됨
    		//증감이 이루어지지 않기 때문에 따로 증감식을 작성해야 함.
    }
    ```
    
    - 조건식이 true일 경우 계속해서 반복
    - 조건식 생략 불가능
    
- **do while 문**
    
    ```java
    do {
    		//반복 수행할 문장
    } while (조건식);
    ```
    
    - 블록 내용을 먼저 수행 후 조건식 판단 (최소 한번은 수행)
    - 조건식이 true일 경우 계속해서 반복
    - 조건식 생략 불가능
    
- **break**
    - switch, while, do-while, for문의 블록에서 빠져나오기 위해 사용
    - 반복문에 이름(라벨)을 붙여 한번에 빠져나올 수 있음
- **continue**
    - 반복문의 특정 지점에서 제어를 반복문의 처음으로 보냄
    - 반복문에 이름(라벨)을 붙여 제어할 수 있음
    

## 배열

- 같은 종류의 데이터를 저장하기 위한 자료구조
- 크기가 고정되어 있음. (한 번 생성된 배열은 크기를 바꿀 수 없음)
- 배열을 객체로 취급
- 배열의 요소를 참조하려면 배열이름과 색인(index)을 사용 ← *index는 정수값이어야 함*

### 배열의 선언

- `type[] variable_name`
- `type variable_name[]`
    
    
    | 타입 | 배열이름 | 선언 |
    | --- | --- | --- |
    | int | iArr | int[] iArr; |
    | char | cArr | char[] cArr; |
    | boolean | bArr | boolean[] bArr; |
    | String | strArr | String[] strArr; |
    | Date | dateArr | Date[] dateArr; |

### 배열의 생성과 초기화

- 자료형[] 배열이름= {값1, 값2, 값3, 값4}; ← 선언과 동시에 초기화
- 배열이름 = new 자료형[] {값1, 값2, 값3, 값4}; ← 배열생성 및 값 초기화
- 배열이름 = new 자료형[길이]; ← 배열 생성(자료형의 기본값으로 초기화)
    
    
    | 자료형 | 기본값 | 비고 |
    | --- | --- | --- |
    | boolean | false |  |
    | char | ‘\u0000’ | 공백문자 |
    | byte, short, int | 0 |  |
    | long | 0L |  |
    | float | 0.0f |  |
    | double | 0.0 |  |
    | 참조형 변수 | null | 아무것도 참조하지 않음 |
    
    ```java
    public calss Array01{
    		public static void main(String[] args){
    				int[] score1;
    				int score1[];
    				// score2 = {1,2,3,4,5}; [X]
    				score2 = new int[] {1,2,3,4,5}; // [O]
    				
    				int[] score3 = {1,2,3,4,5};
    				int[] score4 = new int[5];
    				score4[0] = 1;
    				score4[1] = 2;
    				score4[2] = 3;
    				score4[3] = 4;
    				score4[4] = 5;
    
    				for (int i = 0; i<score4.length; i++) {
    						System.out.println(score4[i]);
    				}
    		}
    }
    ```
    

### 배열의 사용

- index(0부터 시작)로 각 요소에 접근
- `Arr.length`를 통해 배열의 길이 조회 가능
- 배열의 길이는 임의 변경 불가
- 길이 변경을 위해서는 새로운 배열 생성 후 내용을 복사해야 함
- 사용하지 않는 배열은 garbage collection이 알아서 제거

### for-each

- 가독성이 개선된 반복문으로, 배열 및 Collections에서 사용
- index 대신 직접 요소(elements)에 접근하는 변수를 제공
- natually ready only (copied value) ⇒ 값을 수정할 수 없음
- Arrays.toString(배열) : 반복문 없이도 배열 안의 요소를 [값1, 값2, … ] 형태로 출력
    
    ```java
    public class Array_foreach {
    		public static void main(String[] args){
    				int[] arr = {77, 50, 10, 12, 64, 15};
    
    //      배열 출력하는 법 
    //      1. for문
    				for(int i = 0; i < arr.length; i++){
    						System.out.println(arr[i]);
    				}
    
    //      2. for-each문
    				for(int x :arr) {
    						System.out.println(x);
    				}
    
    //      3. 반복문 없이도 가능
    				System.out.println(**Arrays.toString(arr)**);
    		}
    }
    ```
    

### 배열의 복사

- `System.arraycopy(*Object src, int srcPos, Object dest, int destPos, int length*)`
- *src* : 원본 배열
- *srcPos* : 원본 배열 복사 시작 위치 (Pos는 Position의 약어)
- *dest* : 복사할 배열
- *destPos* : 복사 받을 시작 위치
- *length* : 복사할 크기
    
    ```java
    public class Array_copy {
    		public static void main(String[] args) {
    				int[] arr = {77, 50, 10, 12, 64, 15};
    				int[] tmp = new int[arr.length*2];
    
    				for(int i = 0; i < arr.length; i++) {
    						tmp[i] = arr[i];
    				}
    
    				int[] tmp2 = new int[arr.length*2];
    				System.arraycopy(arr, 0, tmp2, 0, arr.length);
    				System.out.println(Arrays.toString(tmp2));
    		}
    }
    ```