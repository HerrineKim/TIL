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

왜 안 하는가? - 이유는 뻔하다. 힘들고, 일정에 치인다. 나중에 나중에 하다가 나중은 절대 오지 않는다. 동질감 자극

그렇지만 TDD에 대해 강조하고 싶다.

TDD는 켄트 백이라는 사람이 TDD라는 책에서 잘 정리했고, 여기서 주요 개념들이 많이 나온다.

TDD의 목표: Clean code that works

TDD = Test First Programming

TDD 사이클 이미지

TDD의 사이클을 보면 간단해 보인다. 하지만 어렵다.

왜? 코드 자체가 테스터블한 코드가 아니기 때문

어떻게? '관심사의 분리' 를 통해 테스터블한 코드를 만들자.

- 자신이 관심 갖는 부분에만 관심을 기울이는 소프트웨어 엔지니어링의 원칙

그렇지 않으면 순식간에 진흙 덩어리가 된다.

[React로 만드는 Todo 앱으로 TDD 시연]

npm run watch 명령어를 사용해 테스팅 툴 jest를 실행해보면 App.js에서 아무런 테스트를 수행하고 있지 않기 때문에 fail한다.

~ 실습 ~

[Redux 왜 쓰는가?]

React의 관심사 때문이다. React의 관심사는 상태의 반영이다. State Reflection.

상태에 대한 관심을 분산하는 것이 중요하다.

Redux 문서를 보면 Presentational Components, Container Components로 구분해 상태는 Container Components 에서만 가져오고 그걸 Presentational에 보여 준다고 한다.

이렇게 책임을 분리하고 특정 컴포넌트의 책임에 집중하면, Single Responsibility Principle을 자연스럽게 지키게 된다. 불필요한 의존성이 줄어들도록 해야 테스트도 원활하게 진행할 수 있기 때문이다.

~Redux 패턴 실습~

1. ListContainer와 테스트 컴포넌트 생성
2. 통과는 되나, 이제 Redux에서 상태관리를 적용해보자.
3. Redux 가짜로 구현
4. fixtures 지정

~실습 하나는 건너 뛰기~

[정리]

TDD는 만능이 아니다

설계 방법론도 아니다

일종의 지뢰 탐지기다.

어찌 보면 뫼비우스의 띠다. 좋은 설계를 하려면 TDD를 잘 해야 하고, TDD를 잘 하려면 좋은 설계가 필요하다.

왜 하느냐? 빅똥과 스몰똥으로 비교할 수 있다. 상대적으로 덩어리가 작을 때 비용이 줄어들 것이다.

결국 미래의 고통을 지금으로 가져오는 기술이다.

TDD를 하기 위해 요구 사항을 명확하게 하는 습관이 생기고, 생각도 잘 해보게 된다는 이점이 있다.

가장 중요한 건 예제로 표현된 스펙이다. 사용 례가 다 나와있고, TDD by example에서도 잘 강조가 되어 있다. 그래서 테스트를 보면 이렇게 이렇게 쓰면 되는 거구나 라는 걸 알 수 있다.

비즈니스 상황에 따라 천천히 도입하고, E2E부터 시작하라. 

:heart:결국 TDD는 테스팅 툴이라기 보다 구현에만 집중하는 것이 아니라 인터페이스에 집중해 코드를 작성해 코드의 퀄리티와 시스템 전반의 설계가 향상될 수 있으며, 개발 집중력도 향상될 수 있다고 한다. 저만 해도 이런 강제성이 없을 때는 컴포넌트를 분리하려는 노력 자체가 크게 줄어든다. Clean code를 위한 원칙을 수립한다는 것에 의미가 있다고 본다.

:heart:그럼 내 코드는 항상 95점짜리냐고 생각할 필요는 없다. TDD 역시 no silver bullet이다. 

:heart:TDD 책 대여!