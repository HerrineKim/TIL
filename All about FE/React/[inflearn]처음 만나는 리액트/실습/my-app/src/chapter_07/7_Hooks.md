# React Hooks

> https://velog.io/@goyou123/React-Hooks-%EC%B4%9D%EC%A0%95%EB%A6%AC

## 소개

> 요약하자면 Hook은 함수형 컴포넌트가 클래스형 컴포넌트의 기능을 사용할 수 있도록 해주는 기능이다.

- React 16.8 버전 (2019년도) 에 추가된 **공식 라이브러리**
- Class형 컴포넌트에서만 쓸 수 있었던 **state와 life cycle을 Function형 컴포넌트에서도 사용 가능**
- 현재 공식문서에서는, Class형 컴포넌트보다는 **Function형 컴포넌트로 새로운 React 프로젝트를 만들기를 권장**
- 단, 기존의 Class형 컴포넌트들을 Hook을 이용한 Function형 컴포넌트로 refactoring할 이유는 전혀 없음



## 왜 필요한가?

> hook을 사용해 함수형 컴포넌트에서도 state와 생명주기를 다룰 수 있기에 **클래스형 컴포넌트에서만 가능하던 상태관리를 더 손쉽게 할 수 있어 필요하다.**

- 함수형 컴포넌트들은 기본적으로 리렌더링이 될때, **함수 안에 작성된 모든 코드가 다시 실행됨**
  \- 클래스형 컴포넌트들은 method의 개념이므로, 리렌더링이 되더라도 render() 를 제외한 나머지 method 및 state는 그대로 보존이 되어 있음.

  

- 이는 함수형 컴포넌트들이 **기존에 가지고 있던 상태(state)를 전혀 관리(기억)할 수 없게 만듦**
  \- 그래서 함수형 컴포넌트를 Stateless Component 라고 했던 것.
  \- 단순하게 React에서의 state 만을 의미하는 것이 아닌, **함수내에 써져 있는 모든 코드 및 변수를 기억할 수 없다는 의미**
  ⇒ ***함수형 컴포넌트가 리렌더링될때 무조건 새롭게 선언 & 초기화 & 메모리에 할당이 됨***

  

- 하지만 Hook의 등장으로, 브라우저에 메모리를 할당 함으로써, **함수형 컴포넌트가 상태(state)를 가질 수 있게 한 것**.
  ⇒ 쉽게 말해서 함수 내에 써져 있는 코드 및 변수를 기억할 수 있게 됐다 라는 의미



- **공식홈페이지에 따르면 Hook을 만든 이유는 다음과 같다.**
  1) 컴포넌트 사이에서 상태 로직 재사용의 어려움 -> render props, HOC 등
  2) 복잡한 (클래스형) 컴포넌트들은 이해하기 어려움 -> 각종 생명주기 함수들
  3) 클래스자체 개념을 이해하기 어려움 -> this 등



## 주의사항

> Hook은 **브라우저의 메모리 자원을 사용하기에 함부로 남발하면 오히려 성능저하**를 불러올 수있다.



## Hook의 규칙

> Hook에는 규칙이 있다. 이를 꼭 지켜야 정상적으로 hook이 실행되고 코드가 꼬이지 않는다.
> eslint-plugin-react-hooks (ESLint 플러그인) 을 사용한다면 아래 두 규칙을 강제한다. (CRA에 포함)

### 1. 최상위에서만 Hook을 호출

- React 함수(컴포넌트)의 최상위에서만 Hook을 호출 할 것.
- 반복문, 조건문, 중첩된 함수등에서 호출 X

### 2. React 함수에서만 Hook을 호출

- Custom Hook에서는 호출 가능
- 일반적인 Javascript 함수에서는 호출 X

### 3. Hook을 만들때 앞에 use 붙히기

- 그래야만 한눈에 보아도 Hook 규칙이 적용되는지를 파악할 수 있기 때문 (공홈)

### 4. React는 Hook 호출되는 순서에 의존

- 한 컴포넌트에서 여러개의 hook이 사용되는 경우
- **hook은 위에서부터 아래로 순서에 맞게 동작한다.**

```javascript
function Form() {
  // 1. name이라는 state 변수를 사용하세요.
  const [name, setName] = useState('Mary');

  // 2. Effect를 사용해 폼 데이터를 저장하세요.
  useEffect(function persistForm() {
    localStorage.setItem('formData', name);
  });

  // 3. surname이라는 state 변수를 사용하세요.
  const [surname, setSurname] = useState('Poppins');

  // 4. Effect를 사용해서 제목을 업데이트합니다.
  useEffect(function updateTitle() {
    document.title = name + ' ' + surname;
  });

  // ...
}
```

- Hook에 호출 순서에 따른 결과

```javascript
// ------------
// 첫 번째 렌더링
// ------------
useState('Mary')           // 1. 'Mary'라는 name state 변수를 선언합니다.
useEffect(persistForm)     // 2. 폼 데이터를 저장하기 위한 effect를 추가합니다.
useState('Poppins')        // 3. 'Poppins'라는 surname state 변수를 선언합니다.
useEffect(updateTitle)     // 4. 제목을 업데이트하기 위한 effect를 추가합니다.

// -------------
// 두 번째 렌더링
// -------------
useState('Mary')           // 1. name state 변수를 읽습니다.(인자는 무시됩니다)
useEffect(persistForm)     // 2. 폼 데이터를 저장하기 위한 effect가 대체됩니다.
useState('Poppins')        // 3. surname state 변수를 읽습니다.(인자는 무시됩니다)
useEffect(updateTitle)     // 4. 제목을 업데이트하기 위한 effect가 대체됩니다.

// ...
```

- 더 자세한 내용은 [공홈 예시](https://ko.reactjs.org/docs/hooks-rules.html) 참고



## Hook의 최적화

### 최적화를 하려면 이런것들을 신경쓰자

> 1. 컴포넌트가 반드시 필요한 리랜더링만을 진행하는가?
> 2. 랜더링이 발생한다면, property 및 method가 반드시 필요한 것만 재할당 할 수 있게 하는가?
> 3. 위 2가지를 무시할만큼, 랜더링이 자주되는가? ) 따라서 메모리를 할당하면서 위의 2가지를 지키지 않아도 되는가?

- 위 3가지 사항이 React가 View Library로서 성능을 최적화에 관여하는 규칙이라고 볼 수 있다.



## Hook을 사용하면 어떤점이 좋은가?

> 기본적으로 클래스형 컴포넌트보다 쉽고 직관적으로 같은 기능을 만들 수 있다.

1. 함수형 컴포넌트로 코드 통일 가능
   - 이전에는 state유무로 있으면 클래스형 / 없으면 함수형으로 분리해서 작업했다고 함
2. **useEffect로 클래스형 Lifecycle에 흩어져 있는 로직 묶음**
   - hook은 Lifecycle과 달리 **여러번 선언가능** 해 코드가 무엇을 하는지에 따라 hook별로 분기가 가능하다.
3. **Custom Hook을 이용해 손쉽게 로직 재사용 가능함**
   - 클래스형 컴포넌트에서 로직을 재사용하기 위해 썼던 HOC나 render-props 같은 패턴이 가져오는 컴포넌트 트리의 불필요한 중첩을 없애줌
   - 커스텀 훅에 관한 자세한 내용은 다음 글 참고



## Hook 종류

> 자체적으로 제공하는 기본 Hook, 추가 Hook이 있고
> 사용자가 만들어서 사용할 수 있는 Custom Hook이 있다.



## 기본 Hooks

1. useState (동적 상태 관리)
2. useEffect (side effect 수행 -mount/unmount/update)
3. useContext (컴포넌트를 중첩하지 않고도 전역 값 쉽게 관리)



## 추가 Hooks

1. useReducer (복잡한 컴포넌트들의 state를 관리 -분리)
2. useCallback (특정 함수 재사용)
3. useMemo (연산한 값 재사용)
4. useRef (DOM선택, 컴포넌트 안에서 조회/수정할 수 있는 변수 관리)
5. useImperativeHandle
6. useLayoutEffect
7. useDebugValue