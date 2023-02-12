# 01-Javascript-기초

[TOC]

# 01-1 Intro

## 브라우저

- URL로 웹(WWW)을 탐색하며 서버와 통신하고, HTML 문서나 파일을 출력하는 GUI 기반의 소프트웨어
- 인터넷의 컨텐츠를 검색 및 열람하도록 함
- '웹 브라우저'라고도 함
- 주요 브라우저
  - Google Chrome, Mozilla Firefox, Microsoft Edge, Opera, Safari

### 브라우저에서 할 수 있는 일

- DOM(Document Object Model) 조작
  - 문서(HTML) 조작
- BOM(Browser Object Model) 조작
  - navigator, screen, location, frames, history, XHR
- Javascript Core(ECMAScript)
  - Data Structure(Object, Array), Conditional Expression, Iteration

### DOM이란?

![image-20221113124748448](01-Javascript-%EA%B8%B0%EC%B4%88.assets/image-20221113124748448.png)

- HTML, XML과 같은 문서를 다루기 위한 프로그래밍 인터페이스
- 문서를 구조화하고, 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
- 문서가 객체(object)로 구조화되어 있으며 key로 접근 가능
- 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
- 주요 객체
  - window: DOM을 표현하는 창(브라우저 탭). 최상위 객체(작성 시 생략 가능)
  - document: 페이지 컨텐츠의 Entry Point 역할을 하며, <head>, <body>와 같은 수많은 다른 요소들을 포함
  - navigator, location, history, screen

#### DOM - 해석

![image-20221113123034892](01-Javascript-%EA%B8%B0%EC%B4%88.assets/image-20221113123034892.png)

- 파싱(Parsing)
  - 구문 분석, 해석
  - 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정

##### DOM - 조작

`document.title`: "네이버"

`document.title = 'Javascript'`

`<- "Javascript"`

#### BOM이란?

- Browser Object Model
- 자바스크립트가 브라우저와 소통하기 위한 모델
- 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
  - 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능
- window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)를 지칭

##### BOM - 조작

![image-20221113124755791](01-Javascript-%EA%B8%B0%EC%B4%88.assets/image-20221113124755791.png)



## Javascript Core

브라우저(BOM & DOM)을 조작하기 위한 명령어 약속(언어)

### Javascript의 필요성

- 브라우저 화면을 '동적'으로 만들기 위함
- 브라우저를 조작할 수 있는 유일한 언어
- Most popular programming language in 2021 survey

### 정리

브라우저(BOM)과 그 내부의 문서(DOM)을 조작하기 위해 ECMAScript(JS)를 학습



## ECMAScript

### ECMA?

- ECMA(ECMA International)
  - 정보 통신에 대한 표준을 제정하는 비영리 표준화 기구
- ECMAScript는 ECMA에서 ECMA-262 규격에 따라 정의한 언어
  - ECMA-262: 범용적인 목적의 프로그래밍 언어에 대한 명세
- ECMAScript6는 ECMA에서 제안하는 6번째 표준 명세를 말함
  - (참고) ECMAScript6의 발표 연도에 따라 ECMAScript2015라고도 불림



## 세미콜론

### 세미콜론

- 자바스크립트는 세미콜론을 선택적으로 사용 가능
- 세미콜론이 없으면 ASI*에 의해 자동으로 세미콜론이 삽입됨
  - ASI: 자동 세미콜론 삽입 규칙(Automatic Semicolon Insertion)



## 코딩 스타일 가이드

- 코딩 스타일의 핵심은 합의된 원칙과 일관성
  - 절대적인 하나의 정답은 없으며, 상황에 맞게 원칙을 정하고 일관성 있게 사용하는 것이 중요
- 코딩 스타일은 코드의 품질에 직결되는 중요한 요소
  - 코드의 가독성, 유지보수 또는 팀원과의 커뮤니케이션 등 개발 과정 전체에 영향을 끼침
- (참고) 다양한 자바스크립트 코딩 스타일 가이드
  - [Airbnb Javascript Style Guide](https://moonspam.github.io/ES5-Airbnb-JavaScript-Style-Guide-Korean/)
  - [Google Javascript Style Guide](https://google.github.io/styleguide/jsguide.html)
  - [standardjs](https://standardjs.com/)



# 01-2 변수와 식별자

## 식별자 정의와 특징

- 식별자(identifier)는 **변수를 구분할 수 있는 변수명**을 말함
- 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작
- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
- 예악어(for, if, function...) 사용 불가능



### 식별자 작성 스타일

- **카멜 케이스(camelCase, lower-camel-case)**
  - **변수, 객체, 함수**에 사용
- **파스칼 케이스(PascalCase, upper-camel-case)**
  - **클래스, 생성자**에 사용
- **대문자 스네이크 케이스(SNAKE_CASE)**
  - **상수(constants)에 사용**
    - 상수의 정의: 개발자의 의도와 상관없이 변경될 가능성이 없는 값을 의미



## 변수 선언 키워드

### let

- 재할당 할 예정인 변수 선언 시 사용
- :star: 변수 재선언 불가능
- 블록 스코프
  - it, for, 함수 등의 중괄호 내부
  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

### const

- :star: 재할당 할 예정이 없는 변수 선언 시 사용
- :star: 변수 재선언 불가능
- 블록 스코프

### 선언, 할당, 초기화

```javascript
let foo // 선언
console.log(foo) // undefined

foo = 11 // 할당
console.log(foo) // 11

let bar = 0 // 선언 + 할당
console.log(bar) // 0
```

- **선언(Declaration)**
  - **변수를 생성**하는 행위 또는 시점
- **할당(Assignment)**
  - 선언된 변수에 값을 저장하는 행위 또는 시점

- **초기화(Initialization)**
  - 선언된 변수에 처음으로 값을 저장하는 행위

### var

- var로 선언한 변수는 재선언 및 재할당 모두 가능
- ES6 이전에 변수를 선언할 때 사용되던 키워드
- 호이스팅*되는 특성으로 인해 예기치 못한 문제 발생 가능
  - 변수를 선언 이전에 참조할 수 있는 현상
  - 변수 선언 이전의 위치에서 접근 시 undefined를 반환
  - 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장
- 함수 스코프*
  - 함수의 중괄호의 내부를 가리킴
  - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능



# 01-3 데이터 타입

## 데이터 타입 종류

- 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐
- 크게 원시 타입(Primitive type)과 참조 타입(Referemce type)으로 분류됨

### 원시 타입

- Number, String, Boolean, undefined, null, Symbol
- 객체(Object)가 아닌 기본 타입
- 변수에 해당 타입의 값이 담김
- 다른 변수에 복사할 때 실제 값이 복사됨

### 숫자(Number) 타입

- 정수, 실수 구분 없느 ㄴ하나의 숫자 타입
- 부동소수점 형식을 따름
- (참고) NaN(Not-A-Number)
  - 계산 불가능한 경우 반환되는 값
  - ex) 'Angel' / 1004 = NaN

### 문자열(String) 타입

- 텍스터 데이터를 나타내는 타입
- 16비트 유니코드 문자의 집합
- 작은 따옴표 또는 큰 따옴표 모두 가능
- 템플릿 리터럴(Template Literal)
  - ES6부터 지원
  - 따옴표대신 backtick(``)으로 표현
  - ${expression} 형태로 표현식 삽입 가능

### Undefined

- 변수의 값이 없음을 나타내는 데이터 타입
- 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined가 할당됨

### null

- 변수의 값이 없음을 :star:의도적으로 표현할 때 사용하는 데이터 타입

- [(참고) null 타입과 typeof 연산자*](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/typeof#null)

  - typeof 연산자*: 자료형 평가를 위한 연산자

  - null 타입은 ECMA 명세의 원시 타입의 정의에 따라 원시 타입에 속하지만, typeof 연산자의 결과는 객체(object)로 표현됨

  - (자바스크립트를 처음 구현할 때, 자바스크립트 값은 타입 태그와 값으로 표시되었습니다. 객체의 타입 태그는 0이었습니다. `null`은 Null pointer(대부분의 플랫폼에서 `0x00`)로 표시되었습니다. 그 결과 null은 타입 태그로 0을 가지며, 따라서 `typeof`는 object를 반환합니다.)

  - ```javascript
    let firstName = null
    console.log(firstName) // null
    
    typeof null // object
    ```

### (참고) undefined 타입과 null 타입 비교

#### undefined

- 빈 값을 표현하기 위한 데이터 타입
- :star:변수 선언 시 아무 값도 할당하지 않으면 자바스크립트가 자동으로 할당
- typeof 연산자의 결과는 undefined

#### null

- 빈 값을 표현하기 위한 데이터 타입
- 개발자가 의도적으로 필요한 경우 할당
- typeof 연산자의 결과는 object



### Boolean 타입

- 논리적 참 또는 거짓을 나타내는 타입
- true 또는 false로 표현
- 조건문 또는 반복문*에서 유용하게 사용
  - (참고)조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 [자동 형변환 규칙](https://ko.javascript.info/type-conversions)에 따라 true 또는 false로 변환됨

### 참조 타입

- Objects
  - Array, Function, ...etc.
  - 객체(object) 타입의 자료형
  - 변수에 해당 객체의 참조 값이 담김
  - 다른 변수에 복사할 때 참조 값이 복사됨



# 01-4 연산자

## 할당 연산자

```javascript
let x = 0

x += 10
console.log(x) // 10

x *= 10
console.log(x) // 70

x /= 10
console.log(x) // 7

x++ // += 연산자와 동일
console.log(x) // 8

x-- // -= 연산자와 동일
console.log(x) // 7
```

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
- 다양한 연산에 대한 단축 연산자 지원



## 비교 연산자

```javascript
const charOne = 'a'
const charTwo = 'z'
console.log(charOne > charTwo) // false
```

- 피연산자들(숫자, 문자, Boolean 등)을 비교하고 결과값을 boolean으로 반환하는 연산자
- 문자열은 유니코드 값을 사용하여 표준 사전 순서를 기반으로 비교
  - ex) 알파벳끼리 비교할 경우
    - 알파벳 순서상 후순위가 더 크다
    - 소문자가 대문자보다 더 크다



## 동등 비교 연산자(==)

```javascript
const a = 1004
const b = '1004'
console.log(a == b) // true

const c = 1
const d = true
console.log(c == d) // true

// 자동 타입 변환 예시
console.log(a + b) // 10041004
console.log(c + d) // 2
```

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 비교할 떄 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음



## 일치 비교 연산자(===)

```javascript
const a = 1004
const b = '1004'
console.log(a === b) // false

const c = 1
const d = true
console.log(c === d) // false
```

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 엄격한 비교*가 이루어지며 암묵적 타입 변환이 발생하지 않음
  - 엄격한 비교*: 두 비교 대상의 타입과 값 모두 같은지 비교하는 방식
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별



## 논리 연산자

- 세 가지 논리 연산자로 구성
  - and 연산은 '&&' 연산자를 이용
  - or 연산은 '||' 연산자를 이용
  - not 연산은 '!' 연산자를 이용
- 단축 평가 지원
  - ex) false && true => false
  - ex) true || false => true




## 삼항 연산자(Ternary Operator)

```javascript
const result = Math.PI > 4 ? 'Yes' : 'No'
console.log(result) // No
```

- 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
- 가장 왼쪽의 조건식이 참이면 콜론(:) 앞의 값을 사용하고 그렇지 않으면 콜론(:) 뒤의 값을 사용
- 삼항 연산자의 결과 값이기 때문에 변수에 할당 가능
- (참고) 한 줄에 표기하는 것을 권장



# 01-5 조건/반복

## 조건문

### 조건문의 종류와 특징

- 'if' statement
  - 조건 표현식의 결과값을 Boolean 타입으로 변환 후 참/거짓을 판단
- 'switch' statement
  - 조건 표현식의 결과값이 **어느 값(case)에 해당하는지 판별**
  - (참고) 주로 특정 변수의 값에 따라 조건을 분기할 때 활용
  - 조건이 많아질 경우 if문보다 가독성이 나을 수 있음

### if statement

```javascript
if (condition) {
    // do something
} else if (condition) {
    // do this
} else {
    // do that
}
```

- if, else if, else
  - 조건은 **소괄호(condition)** 안에 작성
  - 실행할 코드는 **중괄호{}** 안에 작성
  - 블록 스코프 생성

- switch statement

  ```javascript
  switch(expression) {
      case 'first value': {
          // do something
          [break]
      }
      case 'second value': {
          //do this
          [break]
      }
  	[default: {
       	// do something
       }]
  }
  ```

  - **switch**
    - 표현식(expression)의 결과값을 이용한 조건문
    - 표현식의 결과값과 case문의 오른쪽 값을 비교
    - break 및 default문은 [선택적]으로 사용 가능
    - break문이 없는 경우 break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행
    - 블록 스코프 생성



### switch 예시 (1/2) break가 있는 경우

```javascript
const nation = 'Korea'

switch(nation) {
    case 'Korea': {
        console.log('안녕하세요!')
        break
    }
    case 'France': {
        console.log('Bonjour!')
        break
    }
    default: {
        console.log('Hello!')
    }
}
```



### switch 예시 (2/2) break가 없는 경우

> 모두 출력된다. (Fall through)

```javascript
const nation = 'Korea'

switch(nation) {
    case 'Korea': {
        console.log('안녕하세요!')
    }
    case 'France': {
        console.log('Bonjour!')
    }
    default: {
        console.log('Hello!')
    }
}
```



## 반복문

### 반복문의 종류와 특징

- while
- for
- for ... in 
  - 주로 **객체(object)의 속성들을 순회**할 때 사용
  - 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 **권장하지 않음**
- for ... of
  - **반복 가능한(iterable)* 객체를 순회**하며 **값을 꺼낼 때 사용**
    - 반복 가능한(iterable) 객체*의 종류: Array, Map, Set, String 등



### while

```javascript
let i = 0

while (i < 6) {
    console.log(i) // 0, 1, 2, 3, 4, 5
    i += 1
}
```

- while
  - 조건문이 참(true)인 동안 반복 시행
  - 조건은 **소괄호** 안에 작성
  - 실행할 코드는 **중괄호** 안에 작성
  - 블록 스코프 생성



### for

```javascript
for (initialization; condition; expression) {
    // do something
}
```

```javascript
for (let i = 0; i < 6; i++) {
    console.log(i) // 0, 1, 2, 3, 4, 5
}

// 1. 반복문 진입 및 변수 i 선언
for (let i = 0; i < 6; i++) {
    console.log(i)
}

// 2. 조건문 평가 후 코드 블럭 실행
for (let i = 0; i < 6; i++) {
    console.log(i) // 0
}

// 3. 코드 블록 실행 이후 i 값 증가(이후 2~3 반복)
for (let i = 0; i < 6; i++) {
console.log(i) // 0
}
```

- for
  - 세미콜론(;)으로 구분되는 세 부분으로 구성
  - initialization
    - **최초 반복문 진입 시 1회만 실행**되는 부분
  - condition
    - **매 반복 시행 전** 평가되는 부분
  - expression
    - **매 반복 시행 이후** 평가되는 부분
  - 블록 스코프 생성



### for  ... in

```javascript
for (variable in object) {
    // do something
}
```

```javascript
const capitals = {
    korea: 'seoul',
    france: 'paris',
    USA: 'washington D.C.'
}

for (let capital in capitals) {
    console.log(capital) // korea, france, USA
}
```

- for ... in
  - **객체(object)의 속성(key)들을 순회**할 때 사용
  - 배열도 순회 가능하지만 **권장하지 않음**
  - 실행할 코드는 **중괄호** 안에 작성
  - 블록 스코프 생성



### for ... of

```javascript
for (variable of iterables) {
    // do something
}
```

```javascript
const fruits = ['딸기', '바나나', '메론']

for (let fruit of fruits) {
    fruit = fruit + '!'
    console.log(fruit)
}

for (const fruit of fruits) {
    // fruit 재할당 불가
    console.log(fruit)
}
```

- for ... of
  - **반복 가능(iterable) 긱체를 순회**하며 **값을 꺼낼 때 사용**
  - 배열 순회 적합
  - 실행할 코드는 **중괄호** 안에 작성
  - 블록 스코프 생성



# 01-6 함수

## 함수 in JavaScript

- 참조 타입 중 하나로써 function 타입에 속함
- JavaScript에서 함수를 정의하는 방법은 주로 2가지로 구분
  - 함수 선언식(function declaration)
  - 함수 표현식(function expression)
- (참고) JavaScript의 함수는 일급 객체*(First-class citizen)에 해당
  - 일급 객체*: 다음의 조건들을 만족하는 객체를 의미함
    - 변수에 할당 가능
    - 함수의 매개변수로 전달 가능
    - 함수의 반환 값으로 사용 가능



## 함수 선언식(function statement, declaration)

```javascript
function name(args) {
    // do something
}

function add(num1, num2) {
    return num1 + num2
}

add(1, 2)
```

- 함수의 이름과 함께 정의하는 방식
- 3가지 부분으로 구성
  - 함수의 이름(name)
  - 매개변수(args)
  - 몸통(중괄호 내부)



## 함수 표현식(function expression)

```javascript
const name = function (args) {
    // do something
}

const add = function (num1, num2) {
    return num1 + num2
}

add(1, 2)
```

- 함수를 표현식* 내에서 정의하는 방식
  - (참고) 표현식*: 어떤 하나의 값으로 결정되는 코드의 단위
- 함수의 이름을 생략하고 익명 함수*로 정의 가능
  - 익명 함수*(anonymous function): 이름이 없는 함수
  - 익명 함수는 함수 표현식에서만 가능
- 3가지 부분으로 구성
  - 함수의 이름**(생략 가능)**
  - 매개변수(args)
  - 몸통(중괄호 내부)



## 기본 인자(default arguments)

- 인자 작성 시 '=' 문자 뒤 기본 인자 선언 가능

  ```javascript
  const greeting = function (name = 'Anonymous') {
      return `Hi ${name}`
  }
  
  greeting()  // Hi Anonymous
  ```



## 매개 변수와 인자의 개수 불일치 허용

- 매개변수보다 인자의 개수가 많을 경우,

  ```javascript
  const noArgs = function() {
      return 0
  }
  
  noArgs(1, 2, 3)  // 0
  
  const twoArgs = function (arg1, arg2) {
      return [arg1, arg2]
  }
  
  twoArgs(1, 2, 3)  // [1, 2]
  ```

- 매개변수보다 인자의 개수가 적을 경우,

  ```javascript
  
  ```

  

# 01-7 배열, 객체

# 01-8 this

]