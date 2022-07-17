# Git

## 1. Git이란?

- = 분산 버전 관리 프로그램.

  **분산** : 데이터를 중앙 서버에만 저장해놓는 것이 아닌, 분산된 서버에 모두 저장.

  **버전** : 컴퓨터 소프트웨어의 특정 상태

  **관리** : 어떤 일의 사무, 시설이나 물건의 유지 개량

  **프로그램** : 컴퓨터에서 실행될 때 특정 작업을 수행하는 일련의 명령어들의 모음

  *버전관리 = 컴퓨터 소프트웨어의 특정 상태들을 관리하는 것.*

- 코드의 버전(히스토리)을 관리하는 도구

- 개발되어온 과정 파악 가능

- 이전 버전과의 변경 사항 비교 및 분석, 복구 가능

<br/> 

### 1-1. **분산 버전 관리**의 장점 :

중앙 집중식 버전 관리의 경우 중앙 서버에만 데이터가 저장되어있어, 서버 장애 발생 시 버전 관리에 차질이 생길 수 있음.

반면, 분산 버전 관리의 경우, 같은 데이터를 분산된 서버에 모두 저장해두기 때문에, 특정 서버가 장애가 발생하더라도 다른 서버의 데이터를 불러올 수 있음.

<br/> 

### 1-2. **분산 버전 관리 서비스**의 종류 :

- Github : Git 기반의 저장소 서비스. 가장 많이 사용됨.

  [Github](https://www.notion.so/Github-3a26237a33f54e5ebe97844e10ffd39f)

- Gitlab :

- Bitbucket : 

<br/> 

### 1-3. Github

**Github** : Git 기반의 저장소 서비스

**Github**의 장점 : 자신이 작성한 코드를 공유(Open source)하거나, 다른 사용자가 작성한 코드를 사용하여 코드 작성시간을 줄일 수 있음. 깃허브를 통해 다른 사람과 프로젝트 협업도 가능. 가장 많은 사용자를 보유한 분산 버전 관리 프로그램.

*개발자가 깃허브를 써야 하는 이유? : 개발에 대한 성실도, 열정을 보여줄 수 있음. 취업에 도움.*
<br/> <br/> 

### Git과 Github의 차이?

Git: 분산 버전 관리 프로그램

Github : git을 기반으로 한 저장소 서비스

## 2. Git 기본기

### Working Directory

: 내가 작업하고 있는 실제 디렉토리

### Staging Area

: 커밋(Commit)으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳

### Repository

: 특정 디렉토리를 버전 관리하는 저장소

- git init 명령어로 로컬 저장소를 생성
- .git 디렉토리에 버전 관리에 필요한 모든 것이 들어있음.

### 2-1. Git 명령어

- git init : git repository를 생성(초기화)
- git add : 작업한 파일을  Staging Area로 옮겨짐
- git commit -m “(커밋 메시지)” : staged된 파일을 커밋함.
- git config —global [user.name](http://user.name) “이름” : 이름을 등록
- git config —global [user.email](http://user.email) “이메일” : 이메일을 등록
- git log **:** git의 commit 히스토리 보기
    - Q ****: git log 종료
- git diff : 두 commit 간 차이 보기

### 2-2. Git status(상태)

- tracked - 변경사항을 추적하고 있는 상태
- untracked - git이 관리하지 않는 파일
- committed - 커밋이 완료된 상태 (Repository에 반영된 상태)
- modified - git이 관리하며 최신인 상태.
    
    

---

### 2-3. README.md 생성하기

- 새 폴더를 만들고 README.md
- 이 파일을 버전 관리하며 Git을 사용해 보자
    
    *“특정 버전으로 저장한다“ = “커밋(Commit)한다”*
    

### 2-4. Github - Local Repository 연동

- git remote add origin “본인의 깃허브 주소”
- git push -u origin master
- git pull
- git branch —set upstream-to=origin/master master

---

- git clone [repo_url] : remote repo를 로컬로 복사
- git push origin master : local repo의 최신 커밋을 remote repo로 push

### 2-5. **git remote add** vs **git clone**

### 2-6. master/main 개념

-u origin master
