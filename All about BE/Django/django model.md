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
- models 모듈을 통해 어떠한 타입의 DB 컬럼을 정의할 것인지 정의한다.0