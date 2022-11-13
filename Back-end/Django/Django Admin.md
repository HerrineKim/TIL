# Django Admin Site

- 서버의 관리자가 활용하는 페이지.
- Model class를 admin.py에 등록하고 관리한다. django.contrib.auth 모듈에서 제공된다.
- record 생성 여부 확인에 유용하며, 직접 record를 삽입할 수도 있다.



## Admin 생성

1.  ```bash
    $ python manage.py createsuperuser
    ```

2. `admin.py`에 model 등록

   ```python
   # articles/admin.py
   
   from django.contrib import admin
   from .models import Article
   
   # optional) admin 페이지에 출력할 컬럼들 지정
   class ArticleAdmin(admin.ModelAdmin):
       list_display = ('pk', 'little', 'content', 'created_at', 'updated_at',)
   
   # admin site에 register
   admin.site.register(Article)
   ```

   > 다양한 ModelAdmin options
   >
   > https://docs.Djangoproject.com/en/3.2/ref/contrib/admin/#modeladmin-options

3. 서버 실행

4. `/admin`에서 관리자 페이지 로그인
