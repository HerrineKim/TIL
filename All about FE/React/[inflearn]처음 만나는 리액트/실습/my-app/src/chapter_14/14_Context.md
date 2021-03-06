# Context

- Vue의 State와 같은 것.
- 데이터를 한 곳에서 관리
- 렌더링 전에 하위 컴포넌트와 상위 컴포넌트가 통신해야 하는 경우



## 무조건 Context를 사용해야 하는 것은 아니다.

- 컴포넌트와 컨텍스트가 연동되면 재사용성이 떨어지기 때문에, 기존의 Composition 방법이 더 적당할 수 있다.
https://guswnl0610.github.io/react/reactComposition/
- 9강의 element variable을 사용해 컴포넌트를 변수에 저장하여 직접 념겨줄 수 있다.
- 상위 컴포넌트만 너무 복잡해진다는 단점이 있다.
- 하위 컴포넌트를 상위 컴포넌트의 의존성과 분리해야 할 경우 하위 컴포넌트를 여러 개의 변수로 나눠서 전달할 수 있다.



## Context API

- const MyContext =  React.createContext(기본값) 을 통해 생성
- <MyContext.Provider value={값}> 으로 consuming 컴포넌트들을 감싸주면 context 전달 가능. context가 변경될 때 consuming 컴포넌트들은 재랜더링된다.
- JS의 object.is()와 같은 방식으로 값 변경을 관찰
- 매번 모든 consumer 컴포넌트들이 재랜더링 되는 것을 막기 위해 state 선언



## Context 구독 방법

- class형: .contextType (이제 거의 사용하지 않기 때문에 function형을 기억하자)
- function형: .Consumer



## useContext() Hook이 더 좋은 방식

- https://cocoon1787.tistory.com/801
- parameter로 객체를 넣어주어야 한다. consumer나 provider는 안 된다.