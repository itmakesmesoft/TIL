# [Django] Form

## Form

### Django Form

- Django 서버는 들어오는 요청을 모두 수용하고 있는데, 이러한 요청 중에는 비정상적인 혹은 악의적인 요청이 있을 수도 있음.
- 이처럼 사용자가 입력한 데이터가 우리가 원하는 데이터 형식이 맞는지에 대한 유효성 검증이 반드시 필요
- Django Form은 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공하여, 개발자가 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있음
- Django는 Form에 관련된 작업의 세 부분을 처리
    - 렌더링을 위한 데이터 준비 및 재구성
    - 데이터에 대한  HTML Form 생성
    - 클라이언트로부터 받은 데이터 수신 및 처리
    

### Django Form Class

- Form Class는 forms.Form의 상속을 통해 선언
- App 폴더에 forms.py 생성 후 ArticleForm class 선언
    
    ```python
    # articles/forms.py
    from django import forms
    
    class ArticleForm(forms.Form):
        title = forms.CharField(max_length=10)
        content = forms.CharField(widget=forms.Textarea)
    ```
    
    ```html
    {{form.as_p}}
    <input type="submit">
    ```
    
    - form에는 model field와 달리 TextField가 존재하지 않음(widget을 사용하여 구현 가능)
- Django의 HTML input 요소 표현
    - **Form fields**
        - 입력에 대한 유효성 검사 로직 처리
        - 템플릿에서 직접 사용됨
        - Form rendering Options
            - as_p() : 각 필드가 단락(p태그)으로 감싸져서 렌더링
            - as_ul() : 각 필드가 목록항목(ul태그)으로 감싸져서 렌더링
            - as_table() : 각 필드가 테이블(tr태그) 행으로 감싸져서 렌더링
    - **Widgets**
        - 웹페이지의 HTML input 요소 렌더링을 담당하며 유효성 검증과는 관계 없음
            
            ```python
            class ArticleForm(forms.Form):
                NATION_A = 'kr'
                NATION_B = 'ch'
                NATION_C = 'jp'
                NATIONS_CHOICES = [
                    (NATION_A, '한국'),
                    (NATION_B, '중국'),
                    (NATION_C, '일본'),
                ]
            
                title = forms.CharField(max_length=10)
                content = forms.CharField(widget=forms.Textarea)
                nation = forms.ChoiceField(choices=NATIONS_CHOICES)
                # nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)
            ```
            
            [Widgets에 대한 자세한 내용](https://docs.djangoproject.com/ko/3.2/ref/forms/widgets/#built-in-widgets)
            
        

## ModelForm

### Django ModelForm

- Model을 통해 Form class를 만들 수 있는 Helper class
    - ModelForm을 사용하면 models.py과 formspy에서 중복으로 작성되는 부분을 없애고 쉽게 Form을 작성할 수 있음.
- ModelForm은 Form과 같은 방식으로 View 함수에서 사용
    - foms 라이브러리에서 파생된 ModelForm class를 상속받음
- 정의된 ModelForm class 안에 Meta class 선언하여 어떤 모델을 기반으로 Form을 작성할 것인지에 대한 정보를 저장. 이를 통해 데이터 형식에 맞는 태그를 알아서 지정해줌

### Meta class

- ModelForm의 정보를 작성하는 곳
- ModelForm을 사용할 경우 참조할 모델이 있어야 하는데, Meta class의 model 속성이 이를 구성
    - 참조하는 모델에 정의된 field 정보를 Form에 알아서 적용해줌
- fields 속성에 ‘__all__’를 사용하여 모델의 모든 필드를 포함할 수 있음
- 또는 exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수 있음

<aside>
🔎 **Meta Data**
데이터를 표한하기 위한 데이터
ex) 사진 데이터(촬영시각, 렌즈, 조리개 값 등)

</aside>

### 호출과 참조

- **호출** : 함수를 호출하는 것을 의미하고, 반환 값을 가짐
- **참조** : 함수를 호출하지 않고 함수 자체를 그대로 전달하여 다른 함수에서 필요한 시점에 호출하는 경우에 사용. 참조 값을 가짐.

```python
def greeting():
    return "Hello World"

# 호출 => 반환값 출력
print(greeting()) # 안녕하세요

# 참조 => 참조값 출력
print(greeting) # <function greeting at 0x10651caf0>
```

### `is_valid()`

- 유효성 검사를 실행하고, 데이터가 유효한지 여부를 `Boolean` 형태로 반환
- `is_valid()`의 반환 값이 False인 경우 `form.errors` 속성에 유효성 검증 실패 원인이 딕셔너리 형태로 저장됨

### `save()`

- form 인스턴스에 바인딩 된 데이터를 통해 데이터베이스 객체를 만들고 저장
- ModelForm의 하위 클래스는 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정
    - instance 인자가 기입되지 않은 경우 save()는 새 인스턴스를 만듦(CREATE)
    - instance 인자가 기입된 경우 save()는 해당 인스턴스를 수정(UPDATE)
    
    ```python
    # CREATE
    form = ArticleForm(request.POST)
    form.save()
    
    # UPDATE
    form = ArticleForm(request.POST, instance = article)
    form.save()
    ```
    
    - request.POST
        - 사용자가 form을 통해 전송한 데이터(새로운 데이터)
    - instance
        - 수정이 되는 대상 인스턴스
        

### Form vs ModelForm

- **Form**
    - 사용자로부터 받는 데이터가 DB와 연관되지 않은 경우 사용
    ex) 로그인
- **ModelForm**
    - 사용자로부터 받는 데이터가 DB와 연관되어 있는 경우 사용
    ex) 회원가입