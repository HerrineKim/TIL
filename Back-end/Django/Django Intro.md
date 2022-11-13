[TOC]

# django_intro

## Intro

### .gitignore

> git으로 프로젝트 내의 특정 파일/폴더를 관리하지 않기 위한 설정

* git은 프로젝트의 모든 파일/폴더의 변경사항을 관리함. 
* 개발시 개발 소스와 상관없는 파일/폴더(예- 운영체제, 개발환경(IDE, 에디터), 특정 프레임워크/라이브러리)를 `.gitignore`로 관리.
  * 파이썬 예시 - [GitHub](https://github.com/github/gitignore/blob/main/Python.gitignore)
* 이외에도 https://gitignore.io/ 사이트에서 운영체제(mac, windows), 개발환경(Pycharm, visual studio code), 특정 언어 및 환경(Python, Django, Jupyternotebook)을 입력하여 조합된 결과를 활용할 수 있다.
  * 예시 - `django`, `visual studio code`, `windows` 



**설치**

```bash
$ pip install django
```

- 특정 버전 설치

  ```bash
  $ pip install django==3.2.12
  ```

- 설치 확인

  ```bash
  $ pip list
  # python -m django --version
  ```

<br>

**프로젝트 생성**

> **[주의]**
>
> project 를 생성할 때, Python 이나 Django 에서 사용중인 이름은 피해야 한다. 
>
> `-` 도 사용할 수 없다. (ex. django, test, class, django-test...)

```bash
$ django-admin startproject firstpjt .
```

<br>

**서버 실행**

```bash
$ python manage.py runserver
```

<br>

**프로젝트 구조**

- `__init__.py`
  - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
- `settings.py`
  - 웹사이트의 모든 설정을 포함
- `urls.py`
  - 사이트의 url와 view의 연결을 지정
- `wsgi.py`
  - Web Server Gateway Interface
  - 장고 어플리케이션이 웹서버와 연결 및 소통하는 것을 도움
- `asgi.py`
  - Asynchronous Server Gateway Interface
  - 장고 어플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
- `manage.py`
  - Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티


<br>

**Application 생성**

```bash
$ python manage.py startapp articles
```

> 일반적으로 Application명은 `복수형`으로 하는 것을 권장

<br>

### 기본 개발 흐름

![image-20220302134411476](00_django_intro.assets/image-20220302134411476.png)

<br>

**Application 구조**

- `admin.py`
  - 관리자용 페이지 관련 기능을 작성 하는 곳.
- `apps.py`
  - 앱의 정보가 있는 곳. 
  - 우리는 수정할 일이 없다.
- `models.py`
  - 앱에서 사용하는 Model(Database)를 정의하는 곳.
- `tests.py`
  - 테스트 코드를 작성하는 곳.
- `views.py`
  - view가 정의 되는 곳. 

<br>

**Project**

- Project(이하 프로젝트)는 Application(이하 앱)의 집합
- collection of apps
- 프로젝트에는 여러 앱이 포함될 수 있음
- 앱은 여러 프로젝트에 있을 수 있음

<br>

**Application**

- 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담당
- 하나의 프로젝트는 여러 앱을 가짐
- 일반적으로 앱은 하나의 역할 및 기능 단위로 작성함

<br>

**Application 등록**

> 반드시 **app 생성 후 등록** 순서를 지켜야한다.

- 방금 생성한 app을 사용하려면 프로젝트에 등록 해야 한다.

  ```python
  # settings.py
  
  INSTALLED_APPS = [
  	'articles',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

  > INSTALLED_APPS의 app order
  >
  > ```python
  > INSTALLED_APPS = [
  >     # Local apps
  >     'blogs',
  > 
  >     # Third party apps
  >     'haystack',
  > 
  >     # Django apps
  >     'django.contrib.admin',
  >     'django.contrib.auth',
  >     'django.contrib.contenttypes',
  >     'django.contrib.sessions',
  >     'django.contrib.sites',
  > ]
  > ```

<br>

**MTV 패턴**

장고는 MVC(Model-View-Controller)를 기반으로 한 프레임워크다. 하지만 장고에서는 같은 개념을 `MTV(Model - Template - View)`라고 부른다.

참고로 MVC패턴은 `데이터`(model), `사용자 인터페이스`(view), `데이터 처리 로직`(controller)**을 구분해 한 요소가 다른 요소들에게 영향을 주지 않도록 설계하는 방식**인데, 장고도 기본적으로 이 방식을 따르며 명칭이 조금 다를 뿐이다.



1. Model

모델은 데이터베이스에 저장되는 **데이터**를 의미한다. excel과 같은 표의 형태로 정리하여 데이터베이스에 넣는다고 생각하면 된다. 원래 DB를 다루기 위해서는 SQL이라는 언어를 알아야하지만, 장고는 이 SQL을 몰라도 DB 작업을 가능하게 해주는 ORM을 제공하기 때문에 공부할 내용이 훨씬 적다.

> ORM이란?
>
> **Object-Relational Mapping**의 약자로, SQL이라는 언어 대신 데이터베이스를 쉽게 연결해주는 방법.



2. Template

템플릿은 **사용자에게 보여지는 부분**이다. [이전 글](https://velog.io/@hidaehyunlee/Django로-Hello-World-웹사이트-만들기)에서 'Hello World'를 작성했던 html파일이 이 템플릿을 담당한다. [장고 템플릿 시스템 문법](https://opentutorials.org/module/4034/24665)에 맞게 python문법을 활용하여 작성하면 되므로, **다른 작업들과 화면 디자인 작업을 분리**하여 확장성을 극대화 시킬 수 있다다. 즉, 보여지는 부분을 만드는 사람은 그 부분에만 집중하여 만들 수 있게 도와주는 역할을 한다.



3. View

뷰는 웹 요청을 받고, 전달받은 데이터들을 해당 어플리케이션의 로직으로 가공하여, 그 결과를 템플릿에 보내준다. 데이터를 가공하는 처리를 해야한다 싶으면 뷰에서 함수를 작성하면 된다.



4. URLconf (URL 설계)

URL은 **view와 template을 이어주는 역할**을 하고, 이 부분을 만들어 주는 작업을 URLconf라고 한다. 장고 1.x 버전에서는 이부분에서 정규표현식을 사용해 복잡했지만, 장고 2.x 버전은 `path()` 함수를 이용해 그 과정을 훨씬 매끄럽게 다듬어서 공부하기 더 쉬워졌다!



5. 정리

- 데이터저장 형태를 어떻게할지 설정하겠다. → `Model`
- 유저에게 보여지는 화면을 고치고 싶다. → `Template`
- 데이터를 처리해서 가공하고 싶다. → `View`
- 가공한 데이터를 유저가 보는 화면으로 넘겨주고 싶다. → URLconf

자신이 하려는 작업이 무엇인지 파악하면 어느 부분을 작업해야하는지 명확해진다. MTV 패턴을 사용한 작업의 장점이다.



**model**

- 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)

**template**

- 파일의 구조나 레이아웃을 정의
- 실제 내용을 보여주는 데 사용 (presentation)

**view**

- HTTP 요청을 수신하고 HTTP 응답을 반환
- Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
- 그리고 탬플릿에게 응답의 서식 설정을 맡김

<br>

**.py 3대장 기억하기**

- `urls.py` : 주소(URL) 관리
- `views.py` : 페이지 관리 (페이지 하나 당, 하나의 함수)
- `models.py` : 데이터베이스 관리

<br>

**[참고]** `runserver` **Automatic reloading**

- 개발 서버는 요청이 들어올 때마다(코드가 저장될 때 마다) 자동으로 Python 코드를 다시 불러온다. 
- 코드의 변경사항을 반영하기 위해서 굳이 서버를 재가동 하지 않아도 된다. 
- 그러나, 파일을 추가하는 등의 몇몇의 동작(커스텀 필터, 새로운 모듈 추가 등)은 개발 서버가 자동으로 인식하지 못하기 때문에, 이런 상황에서는 서버를 재가동 해야 적용되는 경우도 있다.

<br>

---

<br>

### 요청과 응답

**urls.py**

- 장고 서버로 요청(request)이 들어오면, 그 요청이 어디로 가야하는지 인식하고 관련된 함수(view)로 넘겨준다.

- `views.py` 에서 만든 함수를 연결시켜준다.

- Variable routing을 하는 경우 views.py에서 함수 파라미터로 받아야한다.

  ```python
  # firstpjt/urls.py
  
  from django.contrib import admin
  from django.urls import path
  from articles import views
  
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      # URL을 index/ 들어오면, 
      # index 함수를 실행시킬 것이다.
      path('index/', views.index),    
  ]
  ```

<br>

**views.py**

- HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
- 함수를 정의할 때 반드시 첫번째는 `request`
  * request 객체 정보 : https://docs.djangoproject.com/en/3.2/ref/request-response/
- Model을 통해 요청에 맞는 필요 데이터에 접근
- template에게 HTTP 응답 서식을 맡김
- 함수 return은 `render` 함수 활용
  * https://docs.djangoproject.com/ko/3.2/topics/http/shortcuts/#render
  * 필수 인자
    * request
    * template 이름

```python
# articles/views.py

# index 함수는
# 어떠한 작업을 하고 (아직 쓰지 않음)
# index.html을 랜더링할 것이다.
def index(request):
    # 작업
    return render(request, 'index.html')
```

<br>

**Templates**

- `views.py`에서 지정한 `index.html` 파일을 만들자.

- Django에서 template이라고 부르는 HTML 파일은 기본적으로 
  **app 폴더안의 templates 폴더 안에 위치**한다. 
  
  ```html
  <!-- articles/templates/index.html -->
  
  <h1>만나서 반갑습니다!</h1>
  ```

<br>

### 추가 설정

`LANGUAGE_CODE`

- 모든 사용자에게 제공되는 번역을 결정

- 이 설정이 적용 되려면 `USE_I18N`이 활성화되어 있어야 함

- http://www.i18nguy.com/unicode/language-identifiers.html

  ```python
  # settings.py
  
  LANGUAGE_CODE = 'ko-kr'
  ```

`TIME_ZONE`

- 데이터베이스 연결의 시간대를 나타내는 문자열 지정

- `USE_TZ`가 True이고 이 옵션이 설정된 경우 데이터베이스에서 날짜 시간을 읽으면 UTC 대신 새로 설정한 시간대의 인식 날짜&시간이 반환 됨

- `USE_TZ`이 False인 상태로 이 값을 설정하는 것은 error

- https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

  ```PYTHON
  # settings.py
  
  TIME_ZONE = 'Asia/Seoul'
  ```

`USE_I18N`

- Django의 번역 시스템을 활성화해야 하는지 여부를 지정

`USE_L10N`

- 데이터의 지역화 된 형식(localized formatting)을 기본적으로 활성화할지 여부를 지정
- True일 경우, Django는 현재 locale의 형식을 사용하여 숫자와 날짜를 표시

`USE_TZ`

- datetimes가 기본적으로 시간대를 인식하는지 여부를 지정
- True일 경우 Django는 내부적으로 시간대 인식 날짜 / 시간을 사용

<BR>

---

<br>

## Template

> https://docs.djangoproject.com/en/3.2/topics/templates/#module-django.template
>
> 데이터 표현을 제어하는 도구이자 표현에 관련된 로직

<br>

### Django template language

> https://docs.djangoproject.com/en/3.2/ref/templates/language/
>
> https://docs.djangoproject.com/ko/3.2/ref/templates/builtins/#built-in-template-tags-and-filters

- django template에서 사용하는 built-in template system
- 조건, 반복, 변수 치환, 필터 등의 기능을 제공
- Django 템플릿 시스템은 단순히 Python이 HTML에 포함 된 것이 아님
  - 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
- 파이썬처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 이건 해당 Python 코드로 실행되는 것이 아님

<br>

**syntax**

1. variables

- `{{ variables }}`

- 변수명은 영,숫자와 밑줄(_)의 조합으로 구성될 수 있으나 밑줄로는 시작 할 수 없음
- 변수명에 공백이나 구두점 문자를 사용할 수 없음
- `dot(.)`를 사용하여 변수 속성에 접근

<br>

2. Filters

- `{{ variable|filter }}`
- 표시할 변수를 수정
- 파이프(|)를 사용하여 적용

<br>

3. Tags

- `{% tag %}`
- 출력 테스트를 만들거나 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 보다 복잡한 일들을 수행
- 일부 태그는 시작과 종료 태그가 필요(`{% tag %}` ... `{% endtag %}`)

<br>

4. Comments(주석)

- `{# lorem #}`

<br>

### Template inheritance

> https://docs.python.org/ko/3.9/library/pathlib.html#module-pathlib

- 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤

  - 어떤 템플릿을 상속 받을지

  - 템플릿의 어떤 블록에 해당하는 내용인지

    ```django
    {% extends 'base.html' %}
    
    {% block title %}
    행운로또
    {% endblock %}
    
    {% block content %}
    <h1>로또 번호입니다.</h1>
    <h2>{{ lotto }}</h2>
    {% endblock %}
    ```

    

- 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override) 할 수있는 블록을 정의하는 기본 “skeleton” 템플릿을 만들 수 있음

  ```python
  # settings.py
  
  TEMPLATES = [
      {
          ...,
          'DIRS': [BASE_DIR / 'firstpjt' / 'templates'],
  ...
  ]
  ```

  - `app_name/templates` 디렉토리 외 추가 경로 설정

<br>

**`extends` tag**

- 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
- 반드시 템플릿 최상단에 위치해야 함(== 템플릿의 첫번째 템플릿 태그여야 함)
  - 즉, 2개 이상 사용할 수 없음

<br>

**`block` tag**

- 하위 템플릿에서 재지정(overriden)할 수 있는 블록을 정의

- 하위 템플릿이 채울 수 있는 공간

- 가독성을 높이기 위해 선택적으로 `{% endblock %}` 태그에 이름 지정

  ```django
  {% block content %}
  {% endblock content %}
  ```

<br>

**Template system**

>https://docs.djangoproject.com/ko/3.1/misc/design-philosophies/#template-system

1. 표현과 로직(view)을 분리

- 우리는 템플릿 시스템이 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐이라고 봅니다. 
- 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 합니다.

<br>

2. 중복을 배제

- 대다수의 동적 웹사이트는 공통 헤더, 푸터, 네이게이션 바 같은 사이트 공통 디자인을 갖습니다. 
- Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게 하여 중복 코드를 없애야 합니다. 

<br>

## HTML Form

**HTML `<form>` element**

- 웹에서 사용자 정보를 입력하는 여러 방식(text, button, checkbox, file, hidden, image, password, radio, reset, submit)을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당
- 핵심 속성
  - action : 입력 데이터가 전송될 URL 지정
  - method : 입력 데이터 전달 방식 지정

<br>

**HTML `<input>` element**

- https://developer.mozilla.org/ko/docs/Web/HTML/Element/input
- 사용자로부터 데이터를 입력 받기 위해 사용
- `type` 속성에 따라 동작 방식이 달라짐
- 핵심 속성
  - **name**
  - 중복 가능, 양식을 제출했을 때 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있음
  - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터(name 은 key , value 는 value)로 `?key=value&key=value` 형태로 전달

<br>

### HTTP request methods

**HTTP**

- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
- 웹에서 이루어지는 모든 데이터 교환의 기초
- HTTP는 주어진 리소스가 수행 할 원하는 작업을 나타내는 request methods를 정의

<br>

**GET**

- 서버로부터 **정보를 조회**하는 데 사용
- 데이터를 가져올 때만 사용해야 함
- 데이터를 서버로 전송할 때 body가 아닌 **Query String Parameters**를 통해 전송

<br>

**throw & catch**

- throw

  ```python
  # first_project/urls.py
  
  path('throw/', views.throw),
  ```

  ```python
  # articles/views.py 
  
  def throw(request):
      return render(request, 'throw.html')
  ```

  ```html
  <!-- articles/templates/throw.html -->
  
  <form action="/catch/" method="GET">
    <label for="message">Throw</label>
    <input type="text" id="message" name="message">
    <input type="submit">
  </form>
  ```

- catch

  ```python
  # first_project/urls.py
  
  path('catch/', views.catch),
  ```

  ```python
  # articles/views.py
  
  def catch(request):
      message = request.GET.get('message')
      context = {
          'message': message,
      }
      return render(request, 'catch.html', context)
  ```

  ```django
  <!-- articles/templates/catch.html -->
  
  <h1>너가 던져서 내가 받은건 {{ message }}야!</h1>
  <a href="/throw/">뒤로</a>
  ```

<br>

**Request object** 

> https://docs.djangoproject.com/en/3.1/ref/request-response/#module-django.http

- 요청 간의 모든 정보를 담고 있는 변수
- 페이지가 요청되면 Django는 요청에 대한 메타 데이터를 포함하는 `HttpRequest` 객체를 만들고
- 그런 다음 Django는 적절한 view 함수를 로드하고 `HttpRequest`를 뷰 함수의 첫 번째 인수로 전달. 
- 그리고 각 view는 `HttpResponse` 개체를 반환한다.

<br>

---

<br>

## URLs

> 웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작

<br>

### Variable routing

- 동적 라우팅
  - 주소 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것

```python
# urls.py

urlpatterns = [
    ...,
    # path('hello/<name>/', views.hello),
    path('hello/<str:name>/', views.hello),
]
```

```python
# views.py

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)
```

```django
<!-- hello.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요 {{ name }}님!</h1>
{% endblock %}
```

<br>

### App URL mapping

> 하나의 프로젝트의 여러 앱이 존재한다면, 각각의 앱 안에 urls.py을 만들고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁하게 가능

**두번째 app 생성 및 등록**

```bash
$ python manage.py startapp pages
```

```python
INSTALLED_APPS = [
    'articles',
    'pages',
    ...,
]
```

<br>

```python
# articles/urls.py

from django.urls import path
from . import views 


urlpatterns = [
    path('index/', views.index),
    path('greeting/', views.greeting),
    path('dinner/', views.dinner),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>/', views.hello),
]
```

```python
# pages/urls.py

from django.urls import path


urlpatterns = [

]
```

> [주의] urlpatterns list가 없는 경우 에러가 발생한다.

- django는 명시적 상대경로(`from .module import ..`)를 권장한다.

<br>

### Including other URLconfs

```python
# firstpjt/urls.py

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
```

<br>

`include()`

- 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 도움
- 함수 include()를 만나게 되면, URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달

<br>

### Naming URL patterns

- Django는 URL에 이름을 지정하는 방법을 제공하므로써 뷰 함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있도록 도움

```python
# articles/urls.py

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'),
]
```

<br>

**url tag 사용하기**

```django
<!-- index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요!</h1>
  <a href="{% url 'greeting' %}">greeting</a>
  <a href="{% url 'dinner' %}">dinner</a>
  <a href="{% url 'throw' %}">throw</a>
{% endblock %}
```

<br>

`{% url '' %}`

- 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환
- 템플릿에 URL을 하드 코딩하지 않고도 DRY 원칙을 위반하지 않고 링크를 출력하는 방법

<br>

---

## Namespace

> 개체를 구분할 수 있는 범위를 나타내는 namespace

**두번째 app의 index 페이지 작성**

```python
# pages/urls.py

from django.urls import path
from . import views 


urlpatterns = [
    path('index/', views.index, name='index'),
]
```

```python
# pages/views.py

def index(request):
    return render(request, 'index.html')
```

```django
<!-- pages/templates/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>두번째 앱의 index</h1>
{% endblock %}
```

```django
<!-- articles/templates/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요!</h1>
  <a href="{% url 'greeting' %}">greeting</a>
  <a href="{% url 'dinner' %}">dinner</a>
  <a href="{% url 'dtl_practice' %}">dtl-practice</a>
  <a href="{% url 'throw' %}">throw</a>

  <h2><a href="{% url 'index' %}">두번째 앱 index로 이동</a></h2>
{% endblock %}
```

<br>

**2가지 문제**

1. articles app index 페이지에서 두번째 앱 index로 이동 하이퍼 링크를 클릭 시 현재 페이지로 이동
   - `URL namespace`
2. pages app index url로 이동해도 articles app의 index 페이지 출력
   - `Template namespace`

<br>

### URL namespace

**app_name attribute 작성**

```python
# pages/urls.py

app_name = 'pages'
urlpatterns = [
    path('index/', views.index, name='index'),
]
```

```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...,
]
```

<br>

**`app_name` attribute**

- URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용 할 수 있음
- urls.py에 `app_name` attribute 값 작성

<br>

**참조**

- `:` 연산자를 사용하여 지정
  - 예를들어, app_name이 `articles`이고 URL name이 `index`인 주소 참조는 `articles:index`

<br>

**URL tag 변경**

```django
<!-- articles/templates/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요!</h1>
  <a href="{% url 'articles:greeting' %}">greeting</a>
  <a href="{% url 'articles:dinner' %}">dinner</a>
  <a href="{% url 'articles:throw' %}">throw</a>

  <h2><a href="{% url 'pages:index' %}">두번째 앱 index로 이동</a></h2>
{% endblock %}
```

<br>

### Template namespace

- Django는 기본적으로 `app_name/templates/` 경로에 있는 templates 파일들만 찾을 수 있으며, INSTALLED_APPS에 작성한 app 순서로 tamplate을 검색 후 렌더링

- 임의로 templates의 폴더 구조를 `app_name/templates/app_name` 형태로 변경해 임의로 이름 공간 생성 후 변경된 추가 경로 작성

  ```python
  # articles/views.py
  
  return render(request, 'articles/index.html')
  ```

  ```python
  # pages/views.py
  
  return render(request, 'pages/index.html')
  ```



## Static files

**Static files**

- 정적 파일 
- 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일 
- 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 보여주는 파일 
- 예를 들어, 웹 사이트는 일반적으로 이미지, 자바 스크립트 또는 CSS와 같은 미리 준비된 추가 파일(움직이지 않는)을 제공해야 함 
- Django에서는 이러한 파일들을 “static file”이라 함

> https://docs.djangoproject.com/en/3.1/howto/static-files/#managing-static-files-e-g-images-javascript-css

<br>

### Static files 구성

1. django.contrib.staticfiles 앱이 `INSTALLED_APPS`에 있는지 확인
2. setting.py에 `STATIC_URL` 정의
3. 템플릿에서 static 템플릿 태그를 사용하여 static file이 있는 상대경로를 빌드
4. 앱에 static file 저장하기 (`my_app/static/my_app/sample.jpg`)

<br>

**Django template tag**

- load
  - 사용자 정의 템플릿 태그 세트를 로드
  - 로드하는 라이브러리, 패키지에 등록된 모든 태그와 필터를 로드
- static
  - STATIC_ROOT에 저장된 정적 파일에 연결

<br>

- 이미지 파일 위치 - `articles/static/articles/images/`
- static file 기본 경로
  - `app_name/static/`

<br>

### The staticfiles app

> https://docs.djangoproject.com/en/3.1/ref/contrib/staticfiles/#module-django.contrib.staticfiles

**`STATICFILES_DIRS`**

```python
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

- app/static/ 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
- 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함

<br>

**`STATIC_URL`**

```python
STATIC_URL = '/static/'
```

- STATIC_ROOT에 있는 정적 파일을 참조 할 때 사용할 URL 
- 개발 단계에서는 실제 정적 파일들이 저장되어 있는 app/static/ 경로 (기본 경로) 및STATICFILES_DIRS에 정의된 추가 경로들을 탐색함 
- 실제 파일이나 디렉토리가 아니며, URL로만 존재 비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함

<br>

**`STATIC_ROOT`**

- collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로 
- django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로 
- 개발 과정에서 setting.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않음 
- 직접 작성하지 않으면 django 프로젝트에서는 setting.py에 작성되어 있지 않음 
- 실 서비스 환경(배포 환경)에서 django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함

> [참고] **collectstatic**
>
> - 프로젝트 배포 시 흩어져있는 정적 파일들을 모아 특정 디렉토리로 옮기는 작업
>
> ```python
> # settings.py 예시
> 
> STATIC_ROOT = BASE_DIR / 'staticfiles'
> ```
>
> ```bash
> $ python manage.py collectstatic
> ```

<b

<br>

### static file 사용하기

1. 기본경로

   - `article/static/articles/` 경로에 이미지 파일 위치

     ```django
     <!-- articles/index.html -->
     
     {% extends 'base.html' %}
     {% load static %}
     
     {% block content %}
       <img src="{% static 'articles/sample.png' %}" alt="sample">
       ...
     {% endblock %}
     ```

     - 이미지 파일 위치 - `articles/static/articles/`

    - static file 기본 경로

      - `app_name/static/`

2. 추가 경로

   - `static/` 경로에 CSS 파일 위치

```django
<!-- base.html -->

<head>
  {% block css %}{% endblock %}
</head>
```

```python
# settings.py

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

```django
<!-- articles/index.html -->

{% extends 'base.html' %}
{% load static %}

{% block css %}
  <link rel="stylesheet" href="{% static 'style.css' %}">
{% endblock %}
```

```css
/* static/style.css */

h1 {
    color: crimson;
}
```


<br>



## 관련 문서 정리

| 개념              | 링크                                                         | 비고     |
| ----------------- | ------------------------------------------------------------ | -------- |
| render            | https://docs.djangoproject.com/ko/3.2/topics/http/shortcuts/#render | views    |
| request object    | https://docs.djangoproject.com/en/3.2/ref/request-response/  | views    |
| URL               | https://docs.djangoproject.com/ko/3.2/topics/http/urls/#path-converters | url      |
| template tag      | https://docs.djangoproject.com/en/3.2/ref/templates/builtins/ | template |
| HTTP              | https://developer.mozilla.org/ko/docs/Web/HTTP               | HTTP     |
| template settings | https://docs.djangoproject.com/en/4.0/ref/settings/#templates | settings |

