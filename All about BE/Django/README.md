# Django

## 가상환경

![image-20220308100654001](README.assets/image-20220308100654001.png)

![image-20220308100812379](README.assets/image-20220308100812379.png)

* 만약에 git을 쓰는 경우에는 반드시 `venv/`

![image-20220308100943689](README.assets/image-20220308100943689.png)

## Django 설치 및 프로젝트 생성

![image-20220308101204457](README.assets/image-20220308101204457.png)

![image-20220308101343520](README.assets/image-20220308101343520.png)

## app 생성

* app 생성 
* app 등록
* app `urls.py` 분리

![image-20220308101737801](README.assets/image-20220308101737801.png)

![image-20220308102636047](README.assets/image-20220308102636047.png)

## 요청 처리 흐름

![image-20220308104058613](README.assets/image-20220308104058613.png)

## 모델 활용

### 마이그레이션

![image-20220308125931741](README.assets/image-20220308125931741.png)

* DB 확인

  ![image-20220308130635250](README.assets/image-20220308130635250.png)

* ![image-20220308130509253](README.assets/image-20220308130509253.png)

  ![image-20220308130306116](README.assets/image-20220308130306116.png)

```bash
$ python manage.py makemigrations

# 새로운 필드가 추가되었는데 기본 값이 없다.
# 왜 문제된다? DB에 값이 필수로 설정되어 있어서. 빈 값은 존재할 수 없도록 되어 있어서.
You are trying to add the field 'created_at' with 'auto_now_add=True' to article without a default; the database needs something to populate existing rows.

# 옵션 
# 1. 내가 지금 직접 디폴트값을 줄게 => 
# 2. 미안. 나 종료하고 models.py에서 내가 직접 설정할게
 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option: 1    
# 디폴트 값을 파이썬 문법으로 유효한 것을 입력해.
Please enter the default value now, as valid Python
# 너 이거 DateTime인데.... 2022-03-08 13:17 직접 X 파이썬 코드로 할 수 있도록 도와줌
# 엔터만 누르면 지금 너 timezone에 맞는 현재시간으로 해줄게
You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now  
Type 'exit' to exit this prompt
[default: timezone.now] >>>
Migrations for 'articles':
  articles\migrations\0002_auto_20220308_1314.py
    - Add field created_at to article
    - Add field updated_at to article
```

![image-20220308132449195](README.assets/image-20220308132449195.png)

### 쿼리
```python
pip install django-extensions   #1

INSTALLED_APPS = (
    ...
    'django_extensions',        #2   setting.py 에 추가 하고 나서야
)

python manage.py shell_plus     #3    사용가능
```

https://docs.djangoproject.com/en/3.2/ref/models/querysets/

![image-20220308140213929](README.assets/image-20220308140213929.png)

#### Create

* `save` 메서드가 호출되는 순간 DB에 저장됨
  * id 는 자동으로 값이 증가하며 부여됨 
  * pk 속성도 활용 가능 (primary key라는 뜻)

```python
# 1. 객체 조작 + save
a1 = Article()
a1.title = '제목'
a1.content = '내용'
a1.save() 

# 2. 객체 조작 + save
a2 = Article(title='제목', content='내용')
a2.save()

# 3. create 메서드
a3 = Article.objects.create(title='제목', content='내용')
```

![image-20220308141125055](README.assets/image-20220308141125055.png)

#### Read

##### all()

> 해당 클래스(테이블) 데이터 조회 => QuerySet (객체들로 구성된)

```python
# 1. 전체 데이터 조회
Article.objects.all()
#=> <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
```

##### get()

> 단일 데이터를 조회 => 객체

* 일반적으로 고유한 값(unique)인 경우 사용하는 메서드 

  * 결과가 없는 데이터일 때 에러 발생

  * 결과가 여러 개 있는 경우 에러 발생

* `pk` : primary key는 데이터베이스에서 유일한 값이므로 pk를 기준으로 조회할 때 사용

```python
# 2. 단일 데이터 조회
Article.objects.get(pk=3)
#=> <Article: Article object (3)>

# 2-1. 없는 데이터 => 에러
Article.objects.get(pk=100)
#=> DoesNotExist: Article matching query does not exist.

# 2-2. 여러개 있는 경우 => 에러
Article.objects.get(title='제목')
#=> MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
```

##### filter()

> 여러 데이터를 조회 => QuerySet

```python
Article.objects.filter(title='제목')
#=> <QuerySet [<Article: Article object (1)>, <Article: Article object (5)>]>

Article.objects.filter(title='냉무')
#=> <QuerySet []>
```

#### Update

```python
a2 = Article.objects.get(pk=2)
a2.title = '변경된 제목'
a2.save()
```

#### Delete

##### delete()

```python
a3 = Article.objects.get(pk=3)
a3.delete()
```



## 게시판 만들기

### Create

![image-20220308162507339](README.assets/image-20220308162507339.png)

### Read - 상세보기

![image-20220308165256963](README.assets/image-20220308165256963.png)

### Delete - 삭제 

![image-20220308171726097](README.assets/image-20220308171726097.png)

## 기타

### 템플릿 상속

![image-20220308105409667](README.assets/image-20220308105409667.png)


![image-20220308105310191](README.assets/image-20220308105310191.png)

### redirect

![image-20220308170226801](README.assets/image-20220308170226801.png)

* URL 패턴

![image-20220310102824143](README.assets/image-20220310102824143.png)

### method GET => POST

![image-20220310101946096](README.assets/image-20220310101946096.png)

![image-20220308174605633](README.assets/image-20220308174605633.png)

![image-20220308174859868](README.assets/image-20220308174859868.png)

![image-20220308174923111](README.assets/image-20220308174923111.png)

#### csrf_token

* form 내부에 반드시 `{% csrf_token %}`![image-20220310102249124](README.assets/image-20220310102249124.png)

* input type hidden

![image-20220310102218655](README.assets/image-20220310102218655.png)
