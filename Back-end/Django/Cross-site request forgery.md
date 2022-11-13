# Cross-site request forgery

: CSRF, 사이트 간 요청 위조. 웹 애플리케이션 취약점 중 하나로 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법. Django는 이에 대한 대응 방법으로 middleware와 template tag를 제공한다.



# middleware

: http 요청과 응답 처리 중간에서 작동하는 시스템이다. Django는 http 요청이 들어오면 미들웨어를 거쳐서 해당 URL에 등록되어 있는 view로 연결해주고, http 응답 역시 미들웨어를 거쳐서 내보낸다.

- django에서 프로젝트를 생성하면 미들웨어들이 settings.py.에 기본적으로 등록되어 있다.



## CSRF token 템플릿 태그 

```django
{% csrf token %}
```

- `<form>` 태그 안에 넣는다.
- 사용자의 데이터에 임의의 난수 값을 부여해, 매 요청마다 해당 난수 값을 포함시켜 전송시키도록 한다.
- 이후 서버에서 요청을 받을 때마다 전달 된 token 값이 유효한지 검증한다.
- 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE 등의 method에 적용된다.
- input type이 hidden으로 작성되며, value는 django에서 생성한 hash값으로 설정된다.
  - hash: 복사된 디지털 증거의 동일성을 입증하기 위해 파일 특성을 축약한 암호와 같은 수치로, '디지털 증거의 지문'으로 통한다. 
- 해당 태그 없이 요청을 보내면 django 서버는 403 forbidden을 응답한다.