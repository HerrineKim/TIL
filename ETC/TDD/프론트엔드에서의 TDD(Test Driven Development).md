# 프론트엔드에서의 TDD(Test Driven Development)

## 참고 문헌

[프론트엔드에서 TDD가 가능하다는 것을 보여드립니다.(FEConf 최수형 개발자님 발표)](https://www.youtube.com/watch?v=L1dtkLeIz-M)

[프론트엔드 개발과 테스트 주도 개발(우아한형제들 개발자 김정환님 발표)](https://www.slideshare.net/jeonghwankim11/ss-78600304?refer=%EA%B0%9C%EB%B0%9C%EC%9E%90%EC%8A%A4%EB%9F%BD%EB%8B%A4)

[TDD를 해야 하는 이유(시드웨일 CTO 코딩의 신 아샬)](https://www.youtube.com/watch?v=j09W0KSofOk)

[TDD의 핵심](https://www.youtube.com/watch?v=Bogx86KKp5o)

테스트 주도 개발(도서)

- [한글 정리본](https://www.rinae.dev/posts/tdd-by-example-summary)

클린 코드를 위한 테스트 주도 개발(도서)

클린 코드(도서)

TDD는 설계 방법론이 아니다(강남언니 CTO 이규원님 블로그)

## 기타

https://twitter.com/dylayed/status/1522754982457487361



## 대본

[TDD 가능 보여드립니다.]

테스트 코드 작성하시나요?

왜 안하는가? - 이유는 뻔하다. 힘들고, 일정에 치인다. 나중에 나중에 하다가 나중은 절대 오지 않는다.

그렇지만 TDD에 대해 강조하고 싶다.

TDD는 켄트 백이라는 사람이 TDD라는 책에서 잘 정리했고, 여기서 주요 개념들이 많이 나온다.

TDD의 목표: Clean code that works

TDD = Test First Programming

TDD의 사이클을 보면 간단해보인다.하지만 어렵다.

왜? 코드 자체가 테스터블한 코드가 아니기 때문

어떻게? '관심사의 분리'를 통해 테스터블한 코드를 만들자.

- 자신이 관심 갖는 부분에만 관심을 기울이는 소프트웨어 엔지니어링의 원칙

그렇지 않으면 순식간에 진흙 덩어리가 된다.