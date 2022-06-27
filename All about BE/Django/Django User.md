# Django User

### 회원 관리

### User Model

https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#user-model

* 필수 : `username` , `password`

#### User 생성

https://docs.djangoproject.com/en/4.0/topics/auth/default/

> User는 비밀번호 저장을 암호화 하는 과정이 필요하여 별도의 메서드를 활용한다.

```python
from django.contrib.auth.models import User
user = User.objects.create_user(username='john', password='johnpassword')
```
#### User 인증

> User의 패스워드가 일치하는지 (인증) 확인하는 함수

* 만약 비밀번호가 일치하면 유저 객체, 아니면 None

```python
from django.contrib.auth import authenticate
user = authenticate(username='john', password='secret')
```

![image-20220412104441773](README.assets/image-20220412104441773.png)

## 회원 가입 기능 구현

![image-20220412112318055](README.assets/image-20220412112318055.png)

## 로그인 기능 구현

* [문서](https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.forms.AuthenticationForm)

![image-20220412141242879](README.assets/image-20220412141242879.png)

* [코드](https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L174) 

![image-20220412141416720](README.assets/image-20220412141416720.png)



![image-20220412141822267](README.assets/image-20220412141822267.png)

### 템플릿에서 변수 활용하기

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



#### `django.template.context_processors.request`[¶](https://docs.djangoproject.com/en/4.0/ref/templates/api/#django-template-context-processors-request)

If this processor is enabled, every `RequestContext` will contain a variable `request`, which is the current [`HttpRequest`](https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.HttpRequest).



#### `django.contrib.auth.context_processors.auth`[¶](https://docs.djangoproject.com/en/4.0/ref/templates/api/#django-contrib-auth-context-processors-auth)

- `auth`(*request*)[¶](https://docs.djangoproject.com/en/4.0/ref/templates/api/#django.contrib.auth.context_processors.auth)

  

If this processor is enabled, every `RequestContext` will contain these variables:

- `user` – An `auth.User` instance representing the currently logged-in user (or an `AnonymousUser` instance, if the client isn’t logged in).
- `perms` – An instance of `django.contrib.auth.context_processors.PermWrapper`, representing the permissions that the currently logged-in user has.



### login required

* 비로그인 상태로 글쓰러가기

![image-20220412144616096](README.assets/image-20220412144616096.png)

* login_required

![image-20220412144653639](README.assets/image-20220412144653639.png)

* 로그인 페이지

![image-20220412144718294](README.assets/image-20220412144718294.png)



* 로그인 버튼을 누르면, 해당 URL 그대로 POST 요청

![image-20220412144825144](README.assets/image-20220412144825144.png)

![image-20220412145105640](README.assets/image-20220412145105640.png)

* next가 있으면 next URL로 리다이렉트

![image-20220412145147207](README.assets/image-20220412145147207.png)

### 글 삭제 

> Redirect는 무조건 GET 요청

* 비로그인 상태로 글 삭제를 누르게 된다면, login_required 이후 로그인 페이지로 이동

  ![image-20220412150646109](README.assets/image-20220412150646109.png)

![image-20220412150627634](README.assets/image-20220412150627634.png)

* 로그인 버튼을 누르면 /articles/10/delete/ 리다이렉트! (GET)
* require_POST

![image-20220412150755077](README.assets/image-20220412150755077.png)

* 405 method not allowed 에러가 발생하게 된다.

![image-20220412150827957](README.assets/image-20220412150827957.png)

#### 정리

* `login_required` 는 GET 요청 처리에서만 활용한다.
* 다음 시간에 글 삭제는 본인만 삭제하도록 할 것임.

## logout

* [문서](https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-out)

![image-20220412153344386](README.assets/image-20220412153344386.png)

















































