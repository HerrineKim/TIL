# README

## 설명



- 제목: 프레임워크를 활용한 웹 페이지 구현
- 개요: 영화 추천 서비스의  메인 화면과 기초 기능 만들기
- 목표:
  - HTML, CSS를 통한 웹 페이지 마크업 및 스타일링
  - Bootstrap 컴포넌트 및 그리드 시스템을 활용한 반응형 레이아웃 구성
  - Django web framework를 활용한 웹 서버 구성
  - Django Template System을 활용한 웹 페이지 마크업
- 사용 데이터: TMDB API
- 개발 도구 및 라이브러리:
  - Visual Studio Code
  - Google Chrome Browser
  - Bootstrap v5
  - Django 3.2 +
  - requests



## 단계별 구현 과정



### 01_가상환경 설정

1. ```python
   python -m venv venv
   source python/Scripts/activate
   ```

2. VScode에서 Interpreter 설정 바꿔주기



### 느낀 점

- 활성화를 까먹거나 Interpreter를 선택하지 않으면 가상환경 설정이 소용 없게 되고, 코드 상에서도 에러가 나니 주의해야 한다.



### 02_프로젝트 및 앱 생성, 등록

1. Djangto 및 requirements 설치

2. ```bash
   # 프로젝트 생성 및 서버 잘 실행되는지 확인하기
   django-admin startproject '프로젝트명' .
   pyton manage.py runserver
   ```

3. ```bash
   # 앱 생성
   python manage.py startapp '앱명'
   ```

4. ```python
   # 앱 등록
   # settings.py
   INSTALLED_APPS = [
       '앱명'
       '...'
   ]
   ```

+ +settings

- 언어, 시간대 설정
- templates 폴더 위치 명시



### 느낀 점

- 프로그래밍은 기계와 대화하는 것이다 보니 엄밀한 절차가 무척 중요한 것 같다. 차근차근 순서를 지키지 않으면 완전히 엎고 처음부터 해야 하는 경우도 생기니까 순서를 항상 기억하자.



### 03_U(rls)

- urls.py : view 메소드를 연결하고 요청 url을 정의하는 파일. 도메인 이하를 path라고 하며, 어떤 화면으로 연결할 지 선언하는 것을 라우팅이라고 한다.
- path 함수의 첫 번째 인자는 클라이언트가 요청할 path를 말한다.
- url을 설정하고 views.py에서 정의한 view 메소드와 연결한다.
- 우리에게 필요한 url은 메인 페이지 격인 index, 추천 시스템을 보여주는 recommendation 두 가지이다.

- ```python
  from django.urls import path
  # views를 import 한다.
  from . import views
  
  #
  urlpatterns = [
      path('', views.index, name='index'),
      path('recommendation/', views.recommendation, name='recommendation'),
  ]
  ```



### 04_ V(iews)

```python
# 랜덤 추천을 위해 import random, API 요청을 위해 import requests 한다.
import random
import requests
from django.shortcuts import render
```

```python
# index 함수
def index(request):
    url = 'https://api.themoviedb.org/3/movie/278/recommendations'
    params={
        'api_key' : '키 자리',
        'region': 'KR',
        'language': 'ko'
    }
    # request 양식에 맞춰 json 정보를 불러와 변수에 저장한다.
    response = requests.get(url, params=params).json()
    movies = response.get('results')
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)
```

```python
# recommendation 함수
# index 함수와 동일한 정보를 template에 전달한다.
def recommendation(request):
    url = 'https://api.themoviedb.org/3/movie/278/recommendations'
    params={
        'api_key' : '키 자리',
        'region': 'KR',
        'language': 'ko'
    }
    response = requests.get(url, params=params).json()
    movie = random.choice(response.get('results'))

    context = {
        'movie': movie,
    }
    return render(request, 'movies/recommendation.html', context)
```



### 06_T(emplates)

#### 1. base.html

- `*{%* *extends* *'base.html'* *%}*` 코드로 모든 template들에 상속해줄 template을 만든다.
- bootstrap의 navbar를 이용해 navbar를 만들고, footer와 그 안에 top 버튼도 넣어준다.



#### 2. index.html

- bootstrap의 card 항목을 그대로 가져와서 grid system을 이용해 화면 px에 따라 달리해 배치한다.

- 포스터 이미지, 영화제목, 영화설명이 포함되어야 하는데, index 함수가 views.py에서 넘겨준 'movies'를 이용해 각각 poster_path, title, overview를 뽑아 대체한다. 

  ```django
  {{ movie.title }}
  ```

- 또한 일일이 작성해줄 필요 없이, `movie in movies` 표현을 통해 card를 반복 생성할 수 있다.

  ```python
  {% for movie in movies %}
  {% endfor %%}
  ```

- bootstrap modal

  이미지를 버튼처럼 기능하도록 하여 modal 창을 띄울 수 있다. 문제는 이것을 carousel과 결합하여 받아온 스틸컷 이미지를 띄워야 하는 것인데, 우선 포스터 이미지를 누르면 modal 창이 뜨는 1차 목표는 달성했고, 주말 중에 완전히 완성해보려고 한다.



#### 3. recommendation.html

- 랜덤으로 뽑힌 한 편의 추천 영화의 정보를 index.html과 같이 `{{ movie.title }}`과 같은 형식으로 출력해주는 template이다.



### 느낀 점

- pjt02를 참고해서 json 정보를 받아오는 것까지는 할 수 있었는데, context 내용을 일일이 만드려고 하니 시간 내에 완성하지 못했다. Django만의 문법을 충분히 공부하지 않아서 응용도 어려웠던 것 같다. 전체적인 구조는 이번 주 수업을 통해 거의 이해한 것 같아서 세세한 문법들도 공부해야겠다!
