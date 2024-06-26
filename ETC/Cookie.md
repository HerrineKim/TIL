# 🍪Cookie

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치(placed-on)되는 작은 기록 정보 파일
  - 브라우저(클라이언트)는 쿠키를 로컬에 key-value 형식으로 저장해 놓았다가, 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송한다.
- 사용자의 행동을 추적하거나 쿠키를 훔쳐서 해당 사용자의 계정 접근 권한을 획득할 수도 있다.



## session

- HTTP 쿠키는 상태가 있는 세션을 만들어준다.
- 웹 페이지에 접속하면 요청한 웹 페이지를 받으며 쿠키를 저장하고, 클라이언트가 같은 서버에 재 요청 시 요청과 함께 쿠키도 함께 전송한다.



### Django의 Session

- django의 session은 middleware를 통해 구현된다.
- 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션을 알아내며, 세션 정보는 django DB의 django session 테이블에 저장된다.
- SessionMiddleware: 요청 전반에 걸쳐 세션을 관리
- AuthenticationMiddleware: 세션을 사용하여 사용자를 요청과 연결



## cookie의 사용 목적

1. 세션 관리

   로그인, 아이디 자동 완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리

2. 개인화

   사용자 선호, 테마 등의 설정

3. 트래킹

   사용자 행동을 기록 및 분석



## cookie의 수명

: 쿠키의 수명은 두 가지 방법으로 정의할 수 있다.

1. Session cookies
   - 현재 세션이 종료되면 삭제된다.
   - 브라우저가 현재 세션이 종료되는 시기를 정의한다. ( 일부 브라우저는 다시 시작할 때 세션 복원을 사용해 세션 쿠키가 오래 지속될 수 있도록 함)
2. Persistent cookies(or permanent cookies)
   - Expried 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제한다.