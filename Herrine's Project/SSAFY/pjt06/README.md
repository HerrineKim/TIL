# README

## 1. 목표 

- 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
- Django web framework를 통한 데이터 조작
- ORM에 대한 이해
- DJango ModelForm을 활용한 사용자 요청 데이터 유효성 검증



## 2. 프로젝트 개요

Django 프레임워크의 modelform을 이용하여 영화 정보를 등록할 수 있는 게시판을 만들었습니다.



## 3. 설명 및 느낀 점

### 1) 환경 설정

1. 가상환경 설정
2. makemigrations
3. requirements 모두 설치
4. gitignore 작성



### 2) Urls

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 이미지 업로드를 위한 코드 추가
```

```python
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),    
    path('', views.index, name='index'),
]
```



### 3) Views

### Index

-  index 함수에서는 글들을 번호 역순으로 정렬한 뒤, 글들을 context에 담아 index.html을 렌더링해주는 역할을 한다.

### create

- create 함수에서는 글 작성, 즉 POST 요청을 했는지 또는 폼을 요청하는 GET 요청을 했는지에 따라 if else문으로 나누어준다. 첫째 경우는 유효성 검증을 통과했다면 DB에 저장 후 해당 글의 detail 페이지를 redirect 해주기만 하면 된다. 둘째 경우는 작성할 수 있는 form을 넘겨준다. 만약 POST도, GET 요청도 아니라면 form을 render 해주면 된다.

### detail

- detail 함수는 특정한 하나의 글의 내용을 보여주는 함수다. 이 때문에 특정 pk값의 글을 하나 불러온 후 detail.html을 렌더링해주면 된다.

### delete

- delete 함수는 특정한 하나의 글을 삭제해준다. 특정 pk값의 글을 하나 불러준 후, POST 요청이 맞다면 삭제 작업 후 index 화면으로 redirect 해준다. 만약 정당한 요청이 아니라면 다시 해당 글의 detail 화면으로 redirect 해준다.

### update

- 마지막 update 함수는 글을 수정해주는 함수다. create와 거의 같은 내용으로 이루어져있지만, update할 특정 pk 글을 가져오고, insatnce값을 넣어 기존의 내용을 표시해준다는 점이 다르다.



### 4) Templates

#### create

```django
{% extends 'base.html' %}


{% block content %}
  <h1>CREATE</h1>
  <hr>
  <form action="{% url 'movies:create' %}" method="POST" enctype="multipart/form-data">
    <div class="form-group">
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit" class="btn btn-primary">Submit</button>
    </div>
  </form>
  <br>
  <a class="btn btn-outline-dark btn-sm" href="{% url 'movies:index' %}" role="button">
    BACK
  </a>
{% endblock content %}
```

- modelform을 사용해 글을 등록할 수 있게 한다.
- 밑에는 BACK 버튼을 추가한다.

### detail

```django
{% extends 'base.html' %}


{% block content %}
  <h1>DETAIL</h1>
  <hr>
  <div class="card border-0">
    <div class="card-body mb-5">
      {% comment %} img url 나타내는 법 {% endcomment %}
      <img src="{{ movie.image.url }}" class="card-img-top" alt="...">
      <br>
      <br>
      <h5 class="card-title">
        {{ movie.title }}
      </h5>
      <p>Audience: {{ movie.audience }}</p>
      <p>Release Dates: {{ movie.release_date }}</p>
      <p>Genre: {{ movie.genre }}</p>
      <p>Score: {{ movie.score }}</p>
      <p class="card-text">{{ movie.description}}</p>
      <a class="btn btn-warning btn-sm" href="{% url 'movies:update' movie.pk %}" role="button">
        UPDATE
      </a>
      <br>
      <br>
      <form action="{% url 'movies:delete' movie.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
    </div>
  </div>
  <a class="btn btn-outline-dark btn-sm" href="{% url 'movies:index' %}" role="button">
    BACK
  </a>
{% endblock content %}
```

- bootstrap을 활용해 card 안에 모든 필트 요소들을 넣어준다.
- a태그와 form태그를 이용해 UPDATE, DELETE와 BACK 버튼을 넣어준다.

### index

```django
{% extends 'base.html' %}


{% block content %}
  <h1>INDEX</h1>
  <a href="{% url 'movies:create' %}">CREATE</a>
  <hr>
  {% for movie in movies %}
    <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>
    <p>{{ movie.score }}</p>
    <hr>
  {% endfor %}
{% endblock content %}
```

- 제목과 평점을 게시물 수 만큼 반복하여 출력해준다. DTL for문을 이용한다.

### update

```django
{% extends 'base.html' %}


{% block content %}
  <h1>UPDATE</h1>
  <hr>
  <form action="{% url 'movies:update' movie.pk %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <a href="{% url 'movies:detail' movie.pk %}">back</a>
{% endblock content %}
```

- view로부터 받아온 instance가 포함된 form을 표시해주고, 수정할 수 있게 한다.



### 느낀 점

- 프로그래밍이 다 그런 거겠지만 django 하면서 작은 디테일들 때문에 에러가 뜨는 경험을 정말 많이 해봤다. 처음에는 막 짜증도 나고, 세세하게 찾아보기도 귀찮은 생각이 들었었다. 그런데 이번 프로젝트에서는 예전보다 에러를 만나고도 좀 더 즐겁게(?) 해결할 수 있게 된 것 같다. 여러 번의 프로젝트를 거치면서 참을성이 길러진 것 같아서 뿌듯하기도 했다.
- 싸피를 시작하기 전에는 웹개발이 재미있을까 싶었는데, 생각보다 정말 재미있는 거 같다.  그런데 프론트도 재미있고, 백도 재미있어서 뭔가 갈팡질팡하고 있는 것 같다 ㅋㅋ

- 나는 결국 소비자랑 가깝게 맞닿아있는 부분에서 일을 하고 싶기 때문에, 앞으로는 html, css, javascript 같은 프론트 공부를 깊이 해봐야겠다고 생각한 한 주였다. 