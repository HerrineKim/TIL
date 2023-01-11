# 프론트엔드에서의 TDD(Test Driven Development)

## 참고 문헌

[프론트엔드에서 TDD가 가능하다는 것을 보여드립니다.(FEConf 최수형 개발자님 발표)](https://www.youtube.com/watch?v=L1dtkLeIz-M)

[프론트엔드 개발과 테스트 주도 개발(우아한형제들 개발자 김정환님 발표)](https://www.slideshare.net/jeonghwankim11/ss-78600304?refer=%EA%B0%9C%EB%B0%9C%EC%9E%90%EC%8A%A4%EB%9F%BD%EB%8B%A4)

[TDD를 해야 하는 이유(시드웨일 CTO 코딩의 신 아샬)](https://www.youtube.com/watch?v=j09W0KSofOk)

[TDD의 핵심](https://www.youtube.com/watch?v=Bogx86KKp5o)

테스트 주도 개발(도서)

- [한글 정리본](https://www.rinae.dev/posts/tdd-by-example-summary)

클린 코드 9장(도서)

TDD는 설계 방법론이 아니다(강남언니 CTO 이규원님 블로그)

[TDD는 기존 개발 방법론과 뭐가 다르지?(한빛미디어)](https://www.hanbit.co.kr/channel/category/category_view.html?cms_code=CMS6706987091&amp;cate_cd=)

["TDD는 버그를 없애주나요?" 테스트주도개발에 대한 편견과 오해 바로잡기](https://fastcampus.co.kr/story_article_tdd)(패스트캠퍼스)

[프론트엔드 개발자의 TDD 적응하기](https://blog.wadiz.kr/%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90%EC%9D%98-tdd-%EC%A0%81%EC%9D%91%ED%95%98%EA%B8%B0/)(와디즈 FE 개발팀 홍전일)

[Kent Beck의 테스트 주도 개발 책을 읽고.](Kent Beck의 테스트 주도 개발 책을 읽고.)(Google Firebase Daniel Lee)



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

Redux 문서를 보면 Presentational Components, Container Components로 구분해 상태는 Container Components에서만 가져오고 그걸 Presentational에 보여 준다고 한다.

이렇게 책임을 분리하777고 특정 컴포넌트의 책임에 집중하면, Single Responsibility Principle을 자연스럽게 지키게 된다. 불필요한 의존성이 줄어들도록 해야 테스트도 원활하게 진행할 수 있기 때문이다.

~ Redux 패턴 실습 ~

1. ListContainer와 테스트 컴포넌트 생성
2. 통과는 되나, 이제 Redux에서 상태관리를 적용해보자.
3. Redux 가짜로 구현
4. fixtures 지정

~ 실습 하나는 건너 뛰기 ~

[정리]

~TDD는 만능이 아니다

설계 방법론도 아니다

일종의 지뢰 탐지기다.

어찌 보면 뫼비우스의 띠다. 좋은 설계를 하려면 TDD를 잘 해야 하고, TDD를 잘 하려면 좋은 설계가 필요하다.

왜 하느냐? 빅똥과 스몰똥으로 비교할 수 있다. 상대적으로 덩어리가 작을 때 비용이 줄어들 것이다.

결국 미래의 고통을 지금으로 가져오는 기술이다.

TDD를 하기 위해 요구 사항을 명확하게 하는 습관이 생기고, 생각도 잘 해보게 된다는 이점이 있다.

가장 중요한 건 예제로 표현된 스펙이다. 사용 례가 다 나와있고, TDD by example에서도 잘 강조가 되어 있다. 그래서 테스트를 보면 이렇게 이렇게 쓰면 되는 거구나 라는 걸 알 수 있다.

비즈니스 상황에 따라 천천히 도입하고, E2E부터 시작하라. 

:heart:결국 TDD는 테스팅 툴이라기 보다 구현에만 집중하는 것이 아니라 인터페이스에 집중해 코드를 작성해 코드의 퀄리티와 시스템 전반의 설계가 향상될 수 있으며, 개발 집중력도 향상될 수 있다고 한다. 저만 해도 이런 강제성이 없을 때는 컴포넌트를 분리하려는 노력 자체가 크게 줄어든다. Clean code를 위한 원칙을 수립한다는 것에 의미가 있다고 본다. 좋은 소프트웨어 디자인을 유도하는 방법론이다. 시작부터 테스트를 작성하는 건 내가 작성하는 코드의 사용자의 관점으로 문제를 본다는 걸 의미한다. 유저 입장에선 어떤 인터페이스가 편할지 생각해보고 테스트 코드를 짜며 사용해본다. 디자인의 윤곽이 잡히면 구현 코드를 짜 본다. 다시 테스트 코드를 짜며 나의 코드를 사용해본다. 반복. 탄탄한 테스트를 바탕으로 더욱 더 과감한 리팩터링도 가능하니 구현 토드의 완성도도 높아진다.

:heart:그럼 내 코드는 항상 95점짜리냐고 생각할 필요는 없다. TDD 역시 no silver bullet이다. 

:heart:TDD 책 대여!

:heart:미래 코드를 만질 사람들이 좋아한다.

:heart:당장 TDD를 도입하기는 어렵다면... SRP라도 잘 지키고, 테스트를 최적화 해보자(console 편하게 찍는 도구)

:heart:나의 OCR 코드를 봐라~ 컴포넌트 별 책임이 분리되어 있지 않으니 콘솔을 어디 찍었는지 기억도 나지 않았다.  https://github.com/HerrineKim/chaek-in/blob/master/FE/chaek-in/src/screens/bookRecord/OCRScreen.jsx#L152

### 아샬

TDD의 핵심: 버그가 수정됐는지는 어떻게 알 수 있나? 버그를 재현하는 코드와 버그가 통과하지 못하는 코드 두 가지로 테스트를 작성하면 된다. 암시적으로 이럴 것이다 라고 생각하는 것이 아니라, 예상되는 결과와 결과를 내는 과정을 명확히 적는 것. 이 스펙을 코드에도 적는 것이 TDD의 전부다. 



# Behavior Driven Development

**BDD**는 시나리오를 기반으로 테스트 케이스를 작성하며 함수 단위 테스트를 권장하지 않는다. 이 시나리오는 비개발자가 봐도 이해할 수 있을 정도의 레벨로 작성하는 것을 권장하기 때문에 특수 영어가 없고 이해하기 쉽게 소통 가능한 것은 BDD의 장점으로 기술팀과 비 기술팀 사이에서 협업을 더 효율적으로 진행할 수 있다.

TDD를 근간으로 파생되었기에 테스트 케이스 자체가 요구사양이 되도록 하는 개발 방식이고 "이 클래스가 어떤 행위를 해야한다"라는 개념을 문장으로 작성해 행위를 위한 테스트에 집중을 할 수 있다.



## E2E 테스트 도구 cypress, testcafe, nightwatch