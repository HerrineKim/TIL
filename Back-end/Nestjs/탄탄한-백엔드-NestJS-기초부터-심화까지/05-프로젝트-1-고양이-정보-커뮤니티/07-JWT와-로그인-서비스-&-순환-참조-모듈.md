# JWT와 로그인 서비스 & 순환 참조 모듈

> 이번 시간에는 JWT를 사용해 로그인을 구현 해본다. 로그인을 구현하는 데는 session, cookie를 사용할 수도 있고, JWT를 사용할 수도 있고, 그냥 token을 사용할 수도 있다.
>
> - JWT : https://jwt.io/
> - JWT에 대해 추가 설명된 블로그 글입니다! 꼭 읽어 주세요!
>   https://hudi.blog/self-made-jwt/

[TOC]

# JWT 사용 이유

Web BE뿐만 아니라 APP BE도 지원하도록 폭넓은 지식을 알려 주는 목적이기 때문이다.

## JWT란?

![JWT (JSON Web Token) 이해하기와 활용 방안 - Opennaru, Inc.](07-JWT와-로그인-서비스-&-순환-참조-모듈.assets/JWT_Stacks.png)

JWT는 JSON Web Token의 줄임말로, JSON 포맷을 사용해 사용자 정보를 저장하는 Web token이라고 할 수 있다. 

JWT는 온점(.)을 기준으로 세 부분으로 나눠져 있는데, 각각 헤더, 페이로드, 시그니쳐라고 한다.

### Header

토큰의 타입과 알고리즘을 base64로 인코딩한 것

### Payload

base64 인코딩 데이터(key-value 쌍)

### Signature

Header, Payload를 조합하고 비밀키로 서명한 후, base64로 인코딩

## JWT 로그인의 프로세스

![image-20230102175556698](07-JWT와-로그인-서비스-&-순환-참조-모듈.assets/image-20230102175556698.png)

1. FE에서 Login Request한다. Login API를 Request할 때 필요한 email과 password를 보내면 BE에서는 이것을 secret key로 sign하여 JWT로 만든다.
2. 만들어진 JWT를 FE에게 발급해 준다.
3. FE는 발급된 JWT를 안전한 공간에 저장한다.

### 안전한 공간

보통은 Localstorage나 HTTP only cookie에 저장하는 경우가 많다.