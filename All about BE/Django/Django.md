# Django 알고리즘

* 재사용성 / 모듈화

## 구조 

* 앱 단위의 MTV 패턴

  * `models.py` , `views.py` , `templates/`

  * `urls.py`

    ```python
    # 프로젝트/urls.py
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('articles/', include('articles.urls')),
    ]
    ```

    ```python
    # 개별 app
    # articles/urls.py
    from django.urls import path
    from . import views
    
    app_name = 'articles'
    
    urlpatterns = [
        path('index/', views.index, name='index'),
        path('test/', views.index, name='test'),
    ]
    ```

    * Template에서 사용법 (URL이 변경되더라도 실제 Template 코드를 변경시킬 필요 없어짐)

    ```django
    {% url 'articles:index' %}
    {% url 'myapp:view-name' %}
    ```

    * https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#url

## 기본 요청 처리

https://docs.djangoproject.com/en/3.2/ref/request-response/

> When a page is requested, Django creates an HttpRequest object 
>
> that contains metadata about the request. 
>
> Then Django loads the appropriate view, 
>
> passing the HttpRequest as the first argument to the view function.
>
> Each view is responsible for returning an HttpResponse object.

> 만드는 사람 입장에서!!!!

### URL

> 등록된 urlpatterns에서 탐색 
>
> 왜 이름을 붙였나요? 변수화하려고, 영향 안받게하려고! (views.py, template에서)

```python
urlpatterns = [
    path('index/', views.index, name='index'),
]
```

### View

> V의 역할 : 요청을 받아서 처리하는 역할

> input : passing the HttpRequest as the first argument to the view function.
> 
> return : Each view is responsible for returning an HttpResponse object.

```python
# URL의 특정  변수화해서 사용하는 경우는 추가 인자 설정을 해야함.
def index(request):
    context = {
        
    }
    # Combines a given template with a given context dictionary 
    # and returns an HttpResponse object with that rendered text.
    return render(request, 'articles/index.html', context)
```

### Template

> T의 역할 : HTML을 동적으로 만들어 나갈 수 있도록 (파이썬 코드의 결과와 반복, 조건 등을 통해서)

> 등록된 APP 순서로 탐색 => 다른 앱에 같은 파일이 있으면 안되니까!
>
> settings.py => `APP_DIRS = True`

```django
<!-- articles/templates/aritcles/index.html-->
<h1>{{ name }}</h1>
```

## Form 요청 처리

### Form을 통한 요청

```html
<form action="/search/" method="GET">
  <label for="message">메시지 :</label>
  <input type="text" id="message" name="q">
  <input type="submit" value="얍!">
</form>
```

* 만약 사용자가, python이라고 입력하고 전송을 하면,
  * URL : `/search/?q=python`
    * `/search/` : `form` 태그의 `action`
    * `q` : `input` 태그의 `name`
  * https://developer.mozilla.org/ko/docs/Learn/Common_questions/What_is_a_URL
    * django 개발 환경
      * Domain Name : 127.0.0.1
      * Port: 8000
      * Path : `{% url %}`
        * `/articles/index/`
      * Parameters

### URL

```python
path('search/', views.search, name='search')
```

### View

> /search/?q=python

```python
def search(request):
    q = request.GET.get('q')
    context = {
        'q': q
    }
    return render(request, 'articles/search.html', context)
```

* `request.GET` : URL 파라미터를 딕셔너리 같은 것으로 저장되어 있음.

  > A dictionary-like object containing all given HTTP GET parameters. See the [`QueryDict`](https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.QueryDict) documentation below.

  * https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.HttpRequest.GET
  
	* `/search/?q=python&title=제목&content=내용` 이라면?
	
	    ```python
	    {'q': 'python', 'title': '제목', 'content': '내용'}

### Template

```django
{{ q }}
```

* context 딕셔너리의 키가 `q` 인 값을 출력















