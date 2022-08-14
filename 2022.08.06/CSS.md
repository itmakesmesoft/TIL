# CSS

### CSS(Cascading Style Sheets)

- HTML에 스타일을 지정하기 위한 언어
- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미

### CSS 문법

```css
h1 {
	color: blue;
	font-size: 15px;
}
```

- **선택자(Selector)**
    - 요소 선택자 : HTML 태그를 직접 선택
    - 클래스(class) 선택자 : 마침표(.)로 시작하며, 해당 클래스가 적용된 항목을 선택
    - 아이디(id) 선택자 : #문자로 시작하며, 해당 아이디가 적용된 항목을 선택(단일 id 사용 권장)
- **선언(Declaration)**
- **속성(Property) :** 어떤 스타일 기능을 변경할지 결정
- **값(Value)** : 어떻게 스타일 기능을 변경할지 결정

### CSS 정의 방법

- 인라인(inline)
- 내부 참조(embedding) - <style>
- 외부 참조(link file) - <head>내 <link>를 통해 CSS 파일 불러오기
    
    ```html
    <html>
    		<head>
    				<title>Page</title>
    				<link rel="stylesheet" href="style.css">
    		</head>
    		<body>
    				<h1>Hello World</h1>
    		</body>
    </html>
    ```
    
    ```css
    h1 {
    		color: blue;
    		font-size: 20px;
    }
    ```
    

### CSS 적용 우선순위(Cascading Order)

1. **!important**
2. inline
3. id
4. class, 속성, pseudo-class
5. element, pseudo-element
6. css 파일 로딩 순서

### CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속
- **결합자(Combinators)**
    - 자손 결합자(공백) : SelectorA 하위의 모든 SelectorB 요소
    - 자식 결합자(>) : SelectorA 바로 아래의 SelectorB 요소
    - 일반 형제 결합자(~) : SelectorA의 형제 요소 중 뒤에 위치하는 SelectorB 요소를 모두 선택
    - 인접 형제 결합자(+) : SelectorA의 형제 요소 중 바로 뒤에 위치하는 SelectorB 요소를 선택
    - *`element***:nth-child(n)**` : 부모 엘리먼트의 모든 자식 엘리먼트중 n번째
    - *`element***:nth-of-type(n)**` : 부모 엘리먼트의 특정 자식 엘리먼트중 n번째
- **상속 되는 요소**
    - Text 관련 요소 (font, color, text-align)
    - opacity
    - visibility
- **상속 되지 않는 요소**
    - Box model 관련 요소(width, height, margin, padding, border, box-sizing, display)
    - position 관련 요소(position, top/right/bottom/left, z-index)
    

### CSS 기본 스타일

- **크기 단위**
    - `px` : 모니터 해상도의 한 화소인 픽셀 기준(고정단위)
    - `%` : 백분율 단위
    - `em` : 배수 단위, 요소에 지정된 사이즈에 상대적 사이즈를 가짐. 상속의 영향을 받음.
    - `rem` : 최상위 요소(html) 사이즈를 기준으로 배수 단위를 가짐. 상속의 영향을 받지 않음.
    - viewport : 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
        - vw, vh, vmin, vmax
- **색상 단위**
    - 색상 키워드(`backrgound-color: red;`)
    - RGB 색상(`background-color: rgb(0, 255, 0);`) : 16진수 표기법
        - RGBA(`background-color: rgba(0, 255, 0, 0.5);`) : a(alpha)는 투명도
    - HSL 색상(`background-color: hsl(0, 100%, 50%);`) : 색상, 채도, 명도
    
- **CSS 문서 표현**
    - 텍스트
        - `font-family` : 서체(폰트)
        - `font-style` : 서체 스타일
        - `font-weight` : 폰트 굵기
        - `letter-spacing` : 자간
        - `word-spacing` : 단어 간격
        - `line-height` : 행간
    - `color` : 컬러
    - `background-image` : 배경 이미지
    - `background-color` : 배경 컬러
    - `li`, `ol`, `ul` : 목록
    - `table` : 표

### Box model

- 모든 HTML 요소는 Box 형태로 되어있음
- 왼쪽 위에서 오른쪽 아래로 쌓임
- 하나의 박스는 네 부분(영역)으로 이루어짐
    - `margin` : 테두리 바깥 영역
    - `border` : 테두리
    - `padding` : 테두리 안쪽 여백
    - `content` : 글이나 이미지 등 내용
- Box model 크기
    - `width`
    - `height`
    - `box-sizing: content-box` : padding을 제외한 순수 contents 영역만을 box로 지정
    - `box-sizing: border-box` : border까지의 너비를 box로 지정
    

### Display

- `display: block`
    - 줄 바꿈이 일어나는 요소
    - 화면 크기 전체의 가로 폭을 차지
    - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
- `display: inline`
    - 줄 바꿈이 일어나지 않는 행의 일부 요소
    - content 너비만큼 가로 폭을 차지
    - width, height, margin-top, margin-bottom을 지정할 수 없음
    - 상하 여백은 line-height로 지정
- `display: inline-block`
    - block과 inline 레벨 요소의 특징을 모두 가짐
    - inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
- `display: none`
    - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
    - 이와 비슷한 visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않음

### block level / inline level

- **블록 레벨 요소**
    - `<div>`
    - `<ul>`, `<ol>`, `<li>`
    - `<p>`
    - `<hr>`
    - `<form>`
- **인라인 레벨 요소**
    - `<span>`
    - `<a>`
    - `<img>`
    - `<input>`, `<label>`
    - `<b>`, `<em>`, `<i>`, `<strong>`

### position

- 문서 상 요소의 위치를 지정
- `position: static`
    - 모든 태그의 기본 값 (좌측 상단)
    - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치됨
- 아래는 좌표 property 사용 가능
    - `position: relative` : static 위치를 기준으로 한 상대 위치
    - `position: absolute` : 절대 위치. static이 아닌 가장 가까이 있는 부모, 조상 요소를 기준으로 이동. 레이아웃에서 공간을 차지하지 않음.
    - `position: fixed` : 부모 요소와 관계없이 viewport를 기준으로 한 고정 위치. 스크롤 시에도 항상 같은 곳에 위치함
    - `position: sticky` : 스크롤에 따라 static → fixed로 변경. 평소 static 상태였다가 스크롤 위치가 임계점에 이르면 fixed로 고정됨

### float

- **속성**
    - `none` : 기본값
    - `left` : 요소를 왼쪽으로 띄움
    - `right` : 요소를 오른쪽으로 띄움

### flexbox

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축
    - main axis
    - cross axis
- **구성 요소**
    - Flex Container (부모 요소)
        - flexbox 레이아웃을 형성하는 가장 기본적인 모델
        - flex item들이 놓여있는 영역
        - display 속성을 flex  혹은 inline-flex로 지정
        `display: flex;` `display: inline-flex;`
    - Flex Item (자식 요소)
        - 컨테이너에 속해있는 컨텐츠(박스)
- **flex 속성**
    1. **배치 설정**
        - `flex-direction` : main axis 기준 설정 방향
            - row
            - row-reverse
            - column
            - column-reverse
        - `flex-wrap` : 아이템이 컨테이너 영역을 벗어나지 않도록 하는 속성
            - nowrap : 한 줄에 배치(기본값)
            - wrap : 넘치는 경우 다음 줄에 배치
        - `flex-flow` : flex-direction과 flex-wrap의 shorthand
            - flex-direction과 flex-wrap에 대한 설정 값을 차례로 작성
                
                ex) `flex-flow: row nowrap;`
                
    2. **공간 배분**
        - `justify-content` : main axis를 기준으로 공간 배분
        - `align-content` : cross axis를 기준으로 공간 배분 
        (아이템이 한 줄로 배치되는 경우 확인 불가)
        - 속성 값
            - `flex-start` (기본값) : 아이템들을 axis 시작점으로
            - `flex-end` : 아이템들을 axis 끝 쪽으로
            - `center` : 아이템들을 axis 중앙으로
            - `space-between` : 아이템 사이의 간격을 균일하게 분배
            - `space-around` : 아이템을 두러싼 영역을 균일하게 분배
            - `space-evenly` : 전체 영역에서 아이템 간 간격을 균일하게 분배
        
    3. **정렬**
        - `align-items` (모든 아이템을 cross axis 기준으로)
        - `align-self`  (개별 아이템)
        - 속성 값
            - `stretch` : 컨테이너를 가득 채우는 속성
            - `flex-start` : 위
            - `flex-end` : 아래
            - `center` : 중앙
            - `baseline` : 텍스트 baseline에 기준선을 맞춤
    4. **기타 속성**
        - `flex-grow` : 남은 영역을 아이템에 분배
        - `order` : 배치 순서