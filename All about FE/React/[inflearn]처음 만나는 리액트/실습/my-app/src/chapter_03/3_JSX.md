# JSX

## 1 JSX란?

- JSX(JavaScript XML)는 Javascript에 XML을 추가한 확장한 문법이다. 
-  JSX는 리액트로 프로젝트를 개발할 때 사용되므로 공식적인 자바스크립트 문법은 아니다. 
-  브라우저에서 실행하기 전에 바벨을 사용하여 일반 자바스크립트 형태의 코드로 변환된다.

ex)

```react
// 실제 작성할 JSX 예시
function App() {
	return (
      <h1>Hello, GodDaeHee!</h1>
    );
}

// 위와 같이 작성하면, 바벨이 다음과 같이 자바스크립트로 해석하여 준다.
function App() {
	return React.createElement("h1", null, "Hello, GodDaeHee!");
}
```

- JSX는 하나의 파일에 자바스크립트와 HTML을 동시에 작성하여 편리하다. 
- 자바스크립트에서 HTML을 작성하듯이 하기 때문에 가독성이 높고 작성하기 쉽다.

 

## 2 JSX 문법

> **1. 반드시 부모 요소 하나가 감싸는 형태여야 한다.**

Virtual DOM에서 컴포넌트 변화를 감지할 때 때 효율적으로 비교할 수 있도록 컴포넌트 내부는 하나의 DOM 트리 구조로 이루어져야 한다는 규칙이 있기 때문이다.

ex) 에러 케이스

```react
// Fail to compile
// parsing error : adjacent JSX elements be wrapped in an enclosing tag
// Did you want a JSX fragment <>...</>?
function App() {
	return (
		<div>Hello</div>
		<div>GodDaeHee!</div>
	);
}
```



![img](3_JSX.assets/img.png)



ex) 정상 코드1 (<div></div>)

```react
// div를 사용 하였기 때문에 스타일 적용시 작성한 코드를 div로 한번 더 감쌌다는 부분을 고려해야 한다.
function App() {
	return (
		<div>
			<div>Hello</div>
			<div>GodDaeHee!</div>
		</div>
	);
}
```

 

ex) 정상 코드2 (<Fragment></Fragment>)

```react
// <Fragment>를 사용가능 하지만 <div>태그보다 무거운 편이다.
function App() {
	return (
		<Fragment>
			<div>Hello</div>
			<div>GodDaeHee!</div>
		</Fragment>
	);
}
```

 

ex) 정상 코드3 (<></>)

```react
function App() {
	return (
		<>
			<div>Hello</div>
			<div>GodDaeHee!</div>
		</>
	);
}
```

 

> **2. 자바스크립트 표현식**

- JSX 안에서도 자바스크립트 표현식을 사용할 수 있다. 자바스크립트 표현식을 작성하려면 JSX내부에서 코드를 { }로 감싸주면 된다. 
- 유효한 모든 JavaScript 표현식을 넣을 수 있다.

[https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#%ED%91%9C%ED%98%84(%EC%8B%9D)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#표현(식)) 

```react
function App() {
	const name = 'GodDaeHee';
	return (
		<div>
			<div>Hello</div>
			<div>{name}!</div>
		</div>
	);
}
```

 

> **3. if문(for문) 대신 삼항 연산자(조건부 연산자) 사용**

- if 구문과 for 루프는 JavaScript 표현식이 아니기 때문에 JSX 내부 자바스크립트 표현식에서는 사용할 수 없다.
- 그렇기 때문에 조건부에 따라 다른 렌더링 시 JSX 주변 코드에서 if문을 사용하거나, {}안에서 삼항 연산자(조건부 연산자)를 사용 한다.

 ex) 방법1 외부에서 사용

```react
function App() {
	let desc = '';
	const loginYn = 'Y';
	if(loginYn === 'Y') {
		desc = <div>GodDaeHee 입니다.</div>;
	} else {
		desc = <div>비회원 입니다.</div>;
	}
	return (
		<>
			{desc}
		</>
	);
}
```

 

ex) 방법2 내부에서 사용

```react
function App() {
	const loginYn = 'Y';
	return (
		<>
			<div>
				{loginYn === 'Y' ? (
					<div>GodDaeHee 입니다.</div>
				) : (
					<div>비회원 입니다.</div>
				)}
			</div>
		</>
	);
}
```

 

ex) 방법3 AND연산자(&&) 사용

```react
// 조건이 만족하지 않을 경우 아무것도 노출되지 않는다.
function App() {
	const loginYn = 'Y';
	return (
		<>
			<div>
				{loginYn === 'Y' && <div>GodDaeHee 입니다.</div>}
			</div>
		</>
	);
}
```

 

ex) 방법4 즉시 실행 함수 사용

```react
function App() {
	const loginYn = 'Y';
	return (
		<>
			{
			  (() => {
				if(loginYn === "Y"){
				  return (<div>GodDaeHee 입니다.</div>);
				}else{
				  return (<div>비회원 입니다.</div>);
				}
			  })()
			}
		</>
	);
}
```

 

> **4. React DOM은 HTML 어트리뷰트 이름 대신 camelCase 프로퍼티 명명 규칙을 사용 한다.**

1. JSX 스타일링 
   - JSX에서 자바스크립트 문법을 쓰려면 {}를 써야 하기 때문에, 스타일을 적용할 때에도 객체 형태로 넣어 주어야 한다. 
   - 카멜 표기법으로 작성해야 한다. (font-size => fontSize)

ex) css style 

```react
function App() {
	const style = {
		backgroundColor: 'green',
		fontSize: '12px'
	}
	return (
		<div style={style}>Hello, GodDaeHee!</div>
	);
}
```

 

2.  class 대신 className 
   - 일반 HTML에서 CSS 클래스를 사용할 때에는 class 라는 속성을 사용한다. 
   - JSX에서는 class가 아닌 className 을 사용한다.

ex) className

```react
function App() {
	const style = {
		backgroundColor: 'green',
		fontSize: '12px'
	}
	return (
		<div className="testClass">Hello, GodDaeHee!</div>
	);
}
```

 

> **5. JSX 내에서 주석 사용 방법**

 JSX 내에서 {/*…*/} 와 같은 형식을 사용 한다.

ex)

```react
function App() {
	return (
		<>
			{/* 주석사용방법 */}
			<div>Hello, GodDaeHee!</div>
		</>
	);
}
```

 

시작태그를 여러줄 작성시에는, 내부에서 // 의 형식을 사용할 수 있다.

```react
function App() {
	return (
		<>
			<div
			// 주석사용방법
			>Hello, GodDaeHee!</div>
		</>
	);
}
```

 

개발자가 JSX를 작성하기만 하면, 리액트 엔진은 JSX를 기존 자바스크립트로 해석하여 준다. 이를 '선언형 화면' 기술이라고 한다.

참고 : https://ko.reactjs.org/docs/introducing-jsx.html

출처: https://goddaehee.tistory.com/296 [갓대희의 작은공간:티스토리]

