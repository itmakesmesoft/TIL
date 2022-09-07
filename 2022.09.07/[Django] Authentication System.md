# [Django] Authentication System

## Django Authentication System

- Authentication(인증) : 사용자의 신원 확인
- Authorization(권한, 허가) : 인증된 사용자가 수행할 수 있는 작업 권한 부여
- `django.contrib.auth`
    - [settings.py](http://settings.py)에 포함되어 있으며, INSTALLED_APPS에서 확인 가능
- auth와 관련한 키워드나 경로는 Django 내부적으로 accounts라는 이름을 사용하고 있으므로, 되도록 accounts 앱을 생성하여 사용하는 것을 권장

### Custom User Model

- `AUTH_USER_MODEL`
    - 프로젝트에서 User를 나타낼 때 사용하는 모델(settings.py의 속성값)
- **Custom User Model로 대체하기**
    - AbstractUser를 상속받는 커스텀 User 클래스를 생성(기존 User 클래스도 AbstractUser를 상속받기 때문에 이름만 다를 뿐 같은 동작을 하게 됨)
    - `settings.py`의 `AUTH_USER_MODEL`을 커스텀 User 모델로 지정
    - admin.py에 커스텀 User 모델 등록
    (기본 User 모델이 아니기 때문에 등록하지 않을 경우 admin site에 출력되지 않음)
    - 프로젝트 도중에 AUTH_USER_MODEL 변경은 권장되지 않음
        - 변경 시 모델 관계에 영향을 미치기 때문에 많은 수작업이 필요
        - 프로젝트 시작단계에 진행하는 것을 강력하게 권장
        
        ```python
        # accounts/models.py
        from django.contrib.auth.models import AbstractUser
        
        class User(AbstractUser):
            pass
        ```
        
        ```python
        # settings.py
        AUTH_USER_MODEL = 'accounts.User'
        ```
        
        ```python
        # accounts/admin.py
        from django.contrib import admin
        from django.contrib.auth.admin import UserAdmin
        from .models import User
        
        admin.site.register(User, UserAdmin)
        ```
        
        [커스텀 유저 모델로 대체하는 과정 알아보기](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model)
        

<aside>
🔎 **AbstracUser**
관리자 권한과 함께 완전한 기능을 가지고 있는 User Model을 구현하는 추상 기본 클래스

**Abstract base classes(추상 기본 클래스)**
- 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
- 데이터베이스 테이블을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가됨

</aside>

## Login/Logout

- 로그인은 Session을 생성하는 과정

## Login

### AuthenticationForm

- 로그인을 위한 built-in form
    - 로그인 하고자 하는 사용자 정보를 입력 받음
    - 기본적으로 username과 password를 받아 데이터가 유효한지 검증
- request 를 첫번째 인자로 취함
`AuthenticationForm(request, data = request.POST)`

### login()

- `login(request, user, backend=None)`
- 인증된 사용자를 로그인 시키는 로직으로, view함수에서 사용
- 현재 세션에 연결하려는 인증된 사용자가 있는 경우 사용
- HttpRequest 객체와 User 객체가 필요

### get_user()

- AuthenticationForm의 인스턴스 메서드
- 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

### Authentication with User

- 템플릿에서 인증 관련 데이터를 출력하는 방법
    - `settings.py`의 context processor 설정 덕분에 어느 템플릿에서든 유저 정보에 접근 가능
    - **context processor**
        - 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
        - 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함. 즉, 자주 사용하는 데이터 목록을 미리 템플릿에 로드하는 방식
        - 변수 설정 시 context processor에서 사용하는 변수명과 중복되지 않도록 주의 필요
    - **django.contrib.auth.context_processors.auth**
        - 현재 로그인한 사용자를 나타내는 User 클래스의 인스턴스가 템플릿 변수 `{{ user }}`에 저장됨
        - 클라이언트가 로그인하지 않은 경우, AnonymousUser 클래스의 인스턴스로 생성됨
    

# Logout

### logout(request)

- HttpRequest 객체를 인자로 받고 반환 값이 없음
- 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음
    - 현재 요청에 대한 Session Data를 DB에서 삭제
    - 클라이언트의 쿠키에서도 Session id 삭제

## 회원가입 기능 구현

### UserCreationForm

- 주어진 username과 password로 권한이 없는 새 유저를 생성하는 ModelForm
- 3개의 필드를 가짐
    - username (from the user model)
    - password1
    - password2