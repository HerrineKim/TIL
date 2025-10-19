# Django Model

[TOC]

## Model

- 단일한 데이터에 대한 정보를 가지며, 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함한다.
- 저장된 데이터베이스의 구조(layout)
- Django는 model을 통해 데이터에 접속하고 관리한다.
- 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑 됨



## Database

- 데이터베이스(DB) (SQLite: 기본 Django 데이터베이스 어댑터)
  - 체계화된 데이터의 모임
- 쿼리(Query)
  - 데이터를 조회하기 위한 명령어
  - 조건에 맞는 데이터를 추출하거나 조작하는 명령어
  - "Query를 날린다." == DB를 조작한다.



## Database의 기본 구조

- 스키마(Schema)
  - 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조(structure)
- 테이블(Table)
  - 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합. SQL 데이터베이스에서는 테이블을 관계라고도 한다.
  - 열(column): 필드(field) or 속성, 각 열에는 고유한 데이터 형식이 지정된다.(Integer, Text, Null 등)
  - 행(row): 레코드(record) or 튜플, 테이블의 데이터는 행에 저장된다.
- PK(기본키): 각 행의 고유 값으로 Primary Key로 불린다. 반드시 설정하여야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용된다.



## Model 정리

"웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구"



## `models.py` 작성해보기

```python
# articles/models.py

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```



- 각 모델은 django.models.Model 클래스의 서브 클래스로 표현된다.
  - `django.db.models` 모듈의 Model 클래스를 상속받음

- models 모듈을 통해 어떠한 타입의 DB 컬럼을 정의할 것인지 정의한다.
  - title과 content는 모델의 필드를 나타냄
  - 각 필드는 클래스 속성으로 지정되어 있으며, 각 속성은 각 데이터베이스의 열에 매핑



### 사용 모델 필드(1/2)

- CharField(max_length=None, **options)
  - 길이의 제한이 있는 문자열을 넣을 때 사용
  - CharField의 max_length는 필수 인자
  - **필드의 최대 길이(문자)**, 데이터베이스 레벨과 Django의 유효성 검사(값을 검증하는 것)에서 활용

### 사용 모델 필드(2/2)

- 글자의 수가 많을 때 사용
- max_length 옵션 작성시 자동 양식 필드인 textarea 위젯에 반영은 되지만 모델과 데이터베이스 수준에는 적용되지 않음
  - max_length 사용은 CharField에서 사용해야 함



## Migrations

### Migrations

"Django가 model에 생긴 변화를 반영하는 방법"



### Migrations Commands

```bash
$ python manage.py makemigrations
```

: model을 변경한 것에 기반한 새로운 migration, 즉 설계도를 만든다.



```bash
$ python manage.py migrate
```

: migration을 DB에 반영한다. model에서의 변경 사항과 DB의 스키마가 동기화되게 된다.



```bash
$ python manage.py sqlmigrate 앱이름 0001
```

```bash
BEGIN;
--
-- Create model Article
--
CREATE TABLE "articles_article"
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
"title", varchar(10) NOT NULL, "content" text NOT NULL);
COMMIT;
```

: migration에 대한 SQL 구문을 볼 수 있다.



```bash
$ python manage.py showmigrations 
```

: migrations 설계도들이 migrate 되었는지 확인할 수 있다.



### 실습

#### 1. `makemigrations`

```bash
$ python manage.py makemigrations
```

- 'migrations/0001_initial.py' 생성 확인

#### 2. `migrate`

```bash
$ python manage.py migrate
```

- 0001_initial.py 설계도를 실제 DB에 반영

#### 3. 실제 DB table 확인

VSCode SQLite 확장 프로그램을 통해 확인

#### 4. `sqlmitrate`

```bash
$ python manage.py sqlmigrate app_name 0001
```

- 해당 migrations 설계도가 SQL문으로 해석되어서 동작할지 미리 확인할 수 있음

##### 실제 DB에 전달되는 SQL문

```sqlite
BEGIN;
--
-- Create model Article
--
CREATE TABLE "articles_article"
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
"title" varchar(10) NOT NULL, "content" text NOT NULL);
COMMIT;
```

#### 5. `showmigrations`(1/2)

```bash
$ python manage.py showmigrations
```

migrations 설계도들이 migrate 됐는지 안됐는지 여부를 확인할 수 있음

#### 6. `showmigrations`(2/2)

showmigrations 결과

```bash
admin
[X] 0001_initial
...
```

#### 7. model 수정(1/3)

```python
# articles/models.py

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- 추가 모델 필드 작성 후 `makemigrations` 진행

#### 8. model 수정(2/3)

- created_at 필드에 대한 default 값 설정: 1 입력 후 enter

#### 9. model 수정(3/3)

timezone.now 함수 값 자동 설정

→ 빈 값 상태에서 enter 클릭

→ migrate를 통해 `models.py` 수정사항 반영



## DateField's options

- auto_now_add
  - 최초 생성 일자
  - Django ORM이 최초 insert(테이블에 데이터 입력)시에만 현재 날짜와 시간으로 갱신(테이블에 어떤 값을 최초로 넣을 때)
- auto_now
  - 최종 수정 일자
  - Django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신



# Database API

## DB API

- "DB를 조작하기 위한 도구"
- Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움
- Model을 만들면 Django는 객체들을 만들고 읽고 수정하고 지울 수 있는 database-abstract API를 자동으로 만듦
- database-abstract API 혹은 database-access API라고도 함



## DB API 구문 - Making Queries

`Article.objects.all()`

- Article: Class Name, 모델, 무조건 class로 만들어 줌
- objects: Manager, DB Query와 연동되는 인터페이스. 각 모델은 애플리케이션에서 최소 하나의 매니저를 가진다.
- all(): QuerySet API



## DB API

- Manager
  - DJango 모델에 데이터베이스 query 작업이 제공되는 인터페이스
  - 기본적으로 모든 Django 모델 클래스에 objects라는 Manager를 추가
- QuerySet
  - 데이터베이스로부터 전달받은 객체 목록
  - queryset 안의 객체는 0개, 1개 혹은 여러 개일 수 있음
  - 데이터베이스로부터 조회, 필터, 정렬 등을 수행할 수 있음
