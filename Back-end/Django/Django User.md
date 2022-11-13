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



## 회원 가입 기능 구현

(코드 참고)



## 로그인 기능 구현

(코드 참고)



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







































