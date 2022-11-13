# django model



## Model

- 단일한 데이터에 대한 정보를 가지며, 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함한다.
- 저장된 데이터베이스의 구조(layout)
- Django는 model을 통해 데이터에 접속하고 관리한다.
- 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑 됨



## models.py 작성해보기

```python
# articles/models.py

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```



- 각 모델은 django.models.Model 클래스의 서브 클래스로 표현된다.
- models 모듈을 통해 어떠한 타입의 DB 컬럼을 정의할 것인지 정의한다.



## Migrations

### Migrations

: Django가 model에 생긴 변화를 반영하는 방법



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



