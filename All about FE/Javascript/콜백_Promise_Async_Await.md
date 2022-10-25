# 콜백_Promise_Async_Await

비동기를 처리하는 프로그래밍에는 아래 3가지 방식을 쓸 수 있다.

1. 콜백 함수
2. Promise
3. async/await

아직 나는 코린이기 때문에 해당 방식을 통해 직접 서버에서 방대한 자료를 가지고와서(물론 주어진 과제 정도는 해봤지만..) 수행해본 적은 없지만 여러가지 문서를 읽고 난 뒤에 개념적으로만 정리해보고자 한다.

전 블로그에서도 말했듯이 비동기 코드는 실행 순서를 예측 할 수 없다.
즉 언제 결과값을 받아올 수 있는지 예측할 수 없다는 것이다.

아래 코드를 보자.

```javascript
function first() {
  let value;

  setTimeout(() => {
    value = { name: "MaxlChan", age: 18 };
  }, 3000);  // 서버에서 데이터를 가지고 오는 과정이라 가정(몇초가 걸리는 지 실제로는 모름)

  return value;
}

console.log(first()); // undefined
```

변수 `value`에 객체를 할당(참조)하기 전에 반환했기 때문에, `foo()` 호출문으로 반환된 값은 `undefined`이다.
비동기에 대한 이해가 있다면, 결과가 왜 `undefined`가 나오는 지 금방 알 수 있다.
(`setTimeout`의 delay인자가 `0`일 경우에도 결과는 동일하다)

우리는 분명 몇 초간 통신을 통해 서버에서 가지고 온 데이터를 활용할 수 있어야 한다.
그러면 비동기 함수를 통해서 얻어진 결과(데이터)를 우리는 어떻게 핸들링할 수 있을까?

# Callback 함수

먼저 전통적인 콜백함수를 통한 해결이다.
**콜백 함수는 말 그대로 나중에 호출할 함수를 의미한다.**
콜백함수을 통해서 위 비동기 함수를 통해 얻어진 데이터를 핸들링 해보자.

```javascript
function first(callback) {
  let value;

  setTimeout(() => {
    value = { name: "MaxlChan", age: 18 };
    callback(null, value);
  }, 4000);
}

first(function (error, value) {
  if (error) {
    // 데이터 송신이 실패할 가능성은 언제나 있기 때문에, 콜백 함수는 에러를 핸들링할 수 있어야 한다.
  } else {
    console.log(value); // { name: "MaxlChan", age: 18 }
  }
});
```

`foo`함수의 인자로 콜백함수를 넘겨주고 *비동기 처리가 끝난 후* 콜백함수를 실행하여 정상적으로 데이터를 가지고 왔다.

그런데 만약 그 가지고 온 값을 활용하기 위해 또 특정 비동기 콜백함수(편의상 1 함수로 명명)를 실행해야되는 상황이라면?
1 함수를 통해 가지고 온 값을 또 활용하기 위해 특정 비동기 콜백함수(편의상 2 함수로 명명)를 실행해야되는 상황이라면?
2 함수를 통해 가지고 온 값을 또 활용하기 위해 특정 비동기 콜백함수(편의상 3 함수로 명명)를 실행해야되는 상황이라면?

```javascript
function first(callback) {
  let value;

  setTimeout(() => {
    value = { name: "MaxlChan", age: 18 };
    callback(null, value);
  }, 4000);
}

first(function callbackOne(error, value) {
  if (error) {
    // ErrorHandling
  } else {
    second(value, function callbackTwo(error, value) {
      if (error) {
        // ErrorHandling
      } else {
        third(value, function callbackThree(error, value) {
          if (error) {
            // ErrorHandling
          } else {
            console.log(
              `Final value is ${value}. Here is end of Callback hell...`
            );
          }
        });
      }
    });
  }
});
```

위와 같은 **Callback Hell**이 발생한다.
에러 핸들링도 각 콜백함수마다 해줘야하기 때문에 **가독성은 더욱 떨어진다.**
예전에는 어떻게 이런 코드를 사용했을까 싶을 정도로 딱 보기에 시력과 정신건강에 해로운 코드이다.

지금은 에러 핸들링도 작성되지 않은 간단한 상태이지만
콜백함수 안에 수많은 코드와 로직이 있다고 가정하면, 정말 머리가 아플 것 같다.

또한, 콜백 함수는 다른 코드의 인자로 넘겨줌으로써 제어권 또한 위임한 함수이다.
**즉, 콜백 함수 호출 시점의 권한이 개발자에게 있는 것이 아니라
제어권을 넘겨받은 코드에게 있다는 것이다.**
좀 추상적인 의미로, 우리는 수동적으로 자세로 해당 콜백 함수의 호출을 지켜볼 수 밖에 없다.

다행히도 ES6에서 도입된 `Promise` 덕분에 이러한 비동기 프로그래밍의 난관을 해결해주었다.

# Promise

> - Promise는 어떤 작업의 중간상태를 나타내는 오브젝트 입니다.
>   — 미래에 어떤 종류의 결과가 반환됨을 promise (약속) 해주는 오브젝트라고 보면 됩니다.
> - Promise 객체는 비동기 작업이 맞이할 미래의 완료 또는 실패와 그 결과 값을 나타냅니다.
>   출저 - MDN

위 정의를 내가 이해한 바로 정리하자면

Promise란 비동기 작업이 종료된 후,

1. 실행이 잘 성공했는지
2. 혹은 실패했는지
3. 그럼 성공 or 실패의 결과 값이 무엇인지

위 세가지 내용을 미래(비동기 작업이 종료된 후)에 **반환**해주겠다고 약속해주는 **객체**이다.

## Promise 객체 생성 방법

Promise는 인스턴스 생성처럼 `new` 키워드를 통해 하나의 **객체**를 생성한다.
객체이기 때문에 변수 등에 할당하여 활용이 가능하다.

Promise는 **하나의 콜백함수(여기서의 의미는 비동기 콜백함수가 아님)를 인자**로 받는다.
`new Promise`가 생성되는 즉시
인자로 받아지는 함수도 즉시 실행되며,
그래서 이 함수를 `executor`, 실행자 함수라고도 부른다.

**해당 실행자(executor) 함수는 또 다시 2개 함수(`resolve`, `reject`)를 인자로 받는다.**

실행자 함수가 실행되면, 함수 내부에서는 비동기 작업이 이루어지고
만약 비동기 작업이 성공했을 시에는 그 성공 값을 인자로 `resolve` 함수를 호출하고,
만약 비동기 작업이 실패했을 시에는 그 실패 값을 인자로 `reject` 함수를 호출한다.

```javascript
const successPromise = new Promise(function (resolve, reject) {
  setTimeout(function () {
    resolve("Success");
  }, 3000);
}); // 비동기 작업 완료 후, 성공 값 "Success"를 가진 프로미스 객체(인스턴스)를 생성하고 변수에 할당

const failurePromise = new Promise(function (resolve, reject) {
  setTimeout(function () {
    reject(new Error("Request is failed"));
  }, 3000);
}); // 실패 값 new Error("Request is failed")를 가진 프로미스 객체(인스턴스)를 생성하고 변수에 할당
```

개발자 도구 콘솔 창에서 찍어보면 이렇다.
![img](https://velog.velcdn.com/images%2Fcoin46%2Fpost%2F2a4ff591-4c38-4ca8-9fbd-229e1b58310b%2FScreen%20Shot%202020-08-04%20at%208.12.43%20PM.png)

해당 결과값은 프로미스 객체의 내부 속성이기 때문에 직접 접근은 불가하고,
이 후에 다루는 `then`, `catch` 메서드를 통해서만 접근이 가능하다.

## Promise 객체의 3가지 상태

Promise 객체는 반드시 아래 3가지 상태중 한가지 상태를 갖는다.

- 대기(pending): 이행하거나 거부되지 않은 초기 상태, 즉 약속된 결과 값이 반환되지 않은 상태
- 이행(fulfilled): 연산이 성공적으로 완료된 상태.
- 거부(rejected): 연산이 실패한 상태
  ![img](https://velog.velcdn.com/images%2Fcoin46%2Fpost%2Ffb55cd67-4b62-435d-b700-903e4964d74e%2FScreen%20Shot%202020-08-04%20at%209.53.40%20PM.png)

Promise 객체는 이행이나 거부 상태를 가지게 되면 더이상 그 상태를 바꿀 수 없다
![img](https://velog.velcdn.com/images%2Fcoin46%2Fpost%2F303e0d41-73b2-47b2-bc04-60c11a5919e2%2FScreen%20Shot%202020-08-04%20at%2010.04.23%20PM.png)

## Promise를 통한 비동기 제어 방법

위에서 언급했듯이 프로미스 객체의 결과값은 내부객체이기 때문에 `then`과 `catch`로만 접근이 가능하다.

### then

`then` 메소드는 프로미스가 이행(fulfilled)되었을 때 실행되는 함수이고
함수를 첫 번째 인자로 받는데, 그 함수의 인자는 Promise의 성공 결과 값을 받습니다.

```javascript
const successPromise = new Promise(function (resolve, reject) {
  setTimeout(function () {
    resolve("Success");
  }, 3000);
});

successPromise.then(function (value) {
  console.log(value); // value인자가 결과 값 "Success"임.
});

successPromise.then((value) => console.log(value)); // 위와 동일한 코드
```

사실 then 메소드는 프로미스가 거부(`reject`)된 경우에도
두 번째 인자로 넣어진 함수를 통해 핸들링이 가능하다.

```javascript
const failurePromise = new Promise(function (resolve, reject) {
  setTimeout(function () {
    reject(new Error("Request is failed"));
  }, 3000);
});

failurePromise.then(
  function (value) {
    console.log(value);
  }, // 프로미스가 거부된 상태이기 때문에 첫번째 인자로 넣어진 함수는 실행되지 않음.
  function (err) {
    console.log(err);
  }
); // 프로미스가 거부된 상태이기 때문에 두번째 인자로 넣어진 함수만 실행됨.

failurePromise.then(
  (value) => console.log(value),
  (err) => console.log(err)
); // 위와 동일한 코드
```

위와 같이`then` 메소드는 프로미스가 이행되거나 거부된 2가지 경우 모두 제어가 가능하지만,
통상적으로 `then` 메소드는 인수에 하나만 전달하여, 비동기 작업이 성공적으로 처리된 경우만 다루고
작업이 실패했을 경우는 그 결과 값을 `catch`메소드를 사용하여 제어를 한다.

### catch

`catch` 메소드는 프로미스가 거부(`rejected`)되었을 때 실행되는 함수이고
함수를 인자로 받는데, 그 함수의 인자는 여기서 거부 결과 값을 받습니다.

```javascript
const failurePromise = new Promise(function (resolve, reject) {
  setTimeout(function () {
    reject(new Error("Request is failed"));
  }, 3000);
});

failurePromise
  .then(function (value) { // 거부(실패)된 프로미스는 then 메소드를 통과하고 
    console.log(value);
  })
  .catch(function (error) {
    console.log(error); 
  }); // catch메소드를 실행. error인자가 거부 결과 값임.

failurePromise
  .then((value) => console.log(value))
  .catch((error) => console.log(error)); // 위와 동일한 코드
```

### Promise Chaining

`then`메소드와 `catch`메소드의 반환 값(`return`)은
또 다른 프로미스 객체를 반환하기 때문에, 서로 Chaining이 가능하다.

```javascript
const successPromise = new Promise((resolve, reject) => {
  setTimeout(function () {
    resolve("Success");
  }, 3000);
});

const anotherPromise = (value) => {
  return new Promise((resolve, reject) => {
    setTimeout(function () {
      resolve(`${value} not`);
    }, 1000);
  });
};

successPromise
  .then((value) => `${value} is`) //  `${value} is`를 결과 값으로 가진 Promise 객체 생성
  .then((secondValue) => anotherPromise(secondValue)) // 다른 프로미스가 처리될 때까지 기다리다가 처리가 완료되면 그 결과를 받음.
  .then((thirdValue) => console.log(thirdValue + " impossible"))
  .catch((error) => {
    errorHandling(error);
    return "again?"; // catch 메소드 이후에도 체이닝 가능.
  })
  .then((lastValue) => console.log(lastValue));

// 약 4초 후에 "Success is not impossible"을 출력 
```

여기서 `catch`메소드는 상위에 체이닝되어 있는 어떤 함수에서 에러가 나더라도 에러 핸들링이 가능하다.

```javascript
const successPromise = new Promise((resolve, reject) => {
  setTimeout(function () {
    resolve("Success");
  }, 3000);
});

successPromise
  .then((value) => `${value} is`)
  .then((secondValue) => {
    throw new Error("Error!!");
  }) // 에러 발생
  .then((thirdValue) => console.log("possible")) // 에러가 발생했으므로 통과함.
  .catch((error) => {
    console.log(error); 
  }); // 위 작업 어디에서든지 에러가 발생하면 catch 메소드가 실행됨.
```

### finally

`finally`메소드는 Promise의 성공과 실패에 관계없이 처리만 되면 실행되는 함수이다.
따라서 `finally`에선 프라미스가 성공되었는지, 실패되었는지 알 수 없다.

```javascript
const successPromise = new Promise((resolve, reject) => {
  setTimeout(function () {
    resolve("Success");
  }, 3000);
});

successPromise
  .then((value) => `${value} is`)
  .then((secondValue) => {
    throw new Error("Error!!");
  }) // 에러 발생
  .then((thirdValue) => console.log("possible"))
  .catch((error) => {
    console.log(error);
  })
  .finally(() => console.log("chain end"));
// 위 Promise상태가 어떻든 간에 Promise 객체가 반환되었기 때문에 finally 메소드가 무조건적으로 실행 됨.
```

## Promise.all

`Promise.all`메소드는 배열과 같이 순회 가능한 객체(주로 거의 배열이라고 한다)를 인자로 받는다.
해당 배열 안의 프로미스가 모두 이행되면(배열 요소가 반드시 프로미스일 필요는 없다),
각각의 **프로미스 결과 값을 담은 배열**을
**이행 결과 값으로 새로운 프로미스 객체를 반환**한다.

```javascript
const one = new Promise((resolve, reject) => {
  setTimeout(() => resolve("one"), 1000);
});
const two = new Promise((resolve, reject) => {
  setTimeout(() => resolve("two"), 2000);
});
const three = new Promise((resolve, reject) => {
  setTimeout(() => resolve("three"), 3000);
});

Promise.all([one, two, three]).then((val) => console.log(val));
/* 배열 안 모든 프로미스가 이행된 후(약 3초 이후) 각 이행 결과값을 담은 배열을
   결과값으로 갖는 프로미스 객체가 만들어져
   콘솔에는 ["one", "two", "three"]가 출력됨.*/

Promise.all(["Hi", 123, three]).then((val) => console.log(val));
/* 배열 안 요소가 반드시 프로미스가 아닌 경우에도 가능함.
  하지만 이 경우에도 요소 안애 프로미스가 있다면 프로미스가 이행된 이후에 프로미스 객체가 생성됨.*/
```

하지만 이 때 배열 요소 중 하나의 프로미스라가 거부되는 즉시,
다른 프로미스 이행 여부와 관계없이 해당 거부 사유를 결과 값으로 반환한다.

```javascript
const one = new Promise((resolve, reject) => {
  setTimeout(() => resolve("one"), 1000);
});
const two = new Promise((resolve, reject) => {
  setTimeout(() => resolve("two"), 2000);
});
const three = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error("Error!!")), 3000);
});

Promise.all([one, two, three])
  .then((val) => console.log(val))
  .catch((err) => console.log(err));
  // 다른 프로미스 이행 여부와 관계없이 catch 메소드가 호출
```

반환하는 프로미스의 이행 값은 매개변수로 주어진 프로미스의 순서와 일치하며,
완료 순서에 영향을 받지 않는다.

```javascript
const one = new Promise((resolve, reject) => {
  setTimeout(() => resolve("one"), 3000);
});
const two = new Promise((resolve, reject) => {
  setTimeout(() => resolve("two"), 2000);
});
const three = new Promise((resolve, reject) => {
  setTimeout(() => resolve("three"), 1000);
});

Promise.all([one, two, three]).then((val) => console.log(val));
// ["one", "two", "three"] 출력
// 배열의 첫번째 요소가 가장 마지막으로 이행 값을 반환했지만, 전달된 순서를 유지함.
```

위의 예시처럼 여러가지 비동기 작업을 병렬적으로 실행하는 과정에서
비동기 작업이 시작된 순서를 유지해야 되는 경우라면 `Promise.all`을 활용하면 된다.

## Point of Promise

흔히 프로미스의 장점으로는 콜백 함수를 통한 비동기 처리시 발생하는 **콜백 헬**을 해결하는 것으로만
초점이 맞추어져있는데, 그보다 중요한 2가지 포인트가 있다.

> The point of promises is to give us back functional composition and error bubbling in the async world. They do this by saying that your functions should return a promise, which can do one of two things:
> **- Become fulfilled by a value**
> **- Become rejected with an exception**
> 출처 - https://blog.domenic.me/youre-missing-the-point-of-promises/

즉 비동기 처리 방식에서

- return value를 이용할 수 있다는 점
- error handling이 동기식 코드와 유사하게 쓰일 수 있다는 점

이 2가지가 프로미스의 핵심이라고 한다.

내가 이해한 방식으로 다시 정리하자면,

기존 비동기 세상(콜백 함수를 통한 비동기 처리)에서는 `return`값은 아무런 의미를 갖지 않는다.
왜냐하면 해당 함수 실행문 안에서 또 다른 함수가 실행되고 또 다른 함수가 실행되는 방식이기 때문이다.
그래서 `return`된 값으로 우리가 뭘 다룰 틈도 없이, 비동기 처리가 이루어진다.

하지만 Promise를 이용할 경우, `return`값 가지고 있는 프로미스 객체가 우리 손에 쥐어지기 때문에
동기코드와 마찬가지로, 그 값을 변수에 할당하거나, 다양한 메소드를 사용하는 것과 같이 자유로운 추가 작업이 가능하게 되었다.

또 기존 비동기 세상(콜백 함수를 통한 비동기 처리)에서는 모든 콜백함수에서 각각 에러 핸들링을 해줘야했다.
하지만 마찬가지로 Promise를 이용할 경우 `then`, `catch`등을 통해 에러에 대한 대처가 훨씬 간결해졌고, 이는 동기 방식의 `try{} catch{}` 구문과 흐름이 매우 유사하다.

**결론적으로, Promise의 포인트는
비동기 흐름을 동기적 흐름과 유사하게 만들어주었다는 것에 초점이 있다고 이해했다.**

# async/await

ES8 추가로 도입된 async functions 그리고 await 키워드는
Promise 결과 값을 `then`, `catch`를 통해 다루는 것이 아닌
변수의 담아 동기적 코드처럼 작성해줄 수 있다는 점에서 편리함을 제공한다.

## async

> 먼저 비 동기 함수를 async function으로 만들기 위하여 function()앞에 async keyword를 추가합니다.
> async function()은 await 키워드가 비동기 코드를 호출할 수 있게 해주는 함수 입니다.
> 출저 - MDN

`async` 함수를 실행하게 되면 무조건 `Promise` 객체가 반환된다.
`async` 함수 내에서 `return`은 반환된 `Promise` 객체의 결과(resolve)값이다.

```javascript
async function name() {
  return "chan"; // async function 내부의 return값은 Promise 객체의 결과값을 반환한다.
}

const foo = name(); // 변수 foo에 프로미스 객체가 할당된다.
console.log(foo); // Promise {<fulfilled>: "chan"}
```

## await

`await` 키워드는 반드시 `async`함수 안에서만 사용할 수 있고,
일반 함수에서 사용하면 SyntaxError를 발생시킨다.

`await` 키워드는 Promise 객체를 생성하는 함수 앞에 놓을 수 있고,
자바스크립트가`await` 키워드를 만나게 되면 해당 함수가 Promise 상태가 이행될 때까지 기다렸다가,
이행이 완료되면 그 결과 값을 반환하고 다음 코드를 실행한다.

```javascript
const promise = function () {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve("Done!!"), 2000);
  });
};
async function foo() {
  const result = await promise(); // 프라미스가 이행될 때까지 기다렸다가,
  console.log(result); // 완료 되면 하단의 코드가 이어서 실행됨
}

foo();
```

`await`키워드를 사용하면 기존에 실행 순서가 예측이 불가능했던 비동기 작동 방식이
동기적으로 실행되는 코드처럼 예측 가능해질 수 있다는 점에서 장점을 드러낸다.

```javascript
console.log(1);

const promise = function () {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log(3);
      resolve("two");
    }, 3000);
  });
};

const promiseTwo = function () {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("one");
    }, 1000);
  });
};

console.log(2);

async function foo() {
  const result = await promise(); // 프라미스가 이행될 때까지 아래 코드로 넘어가지 않음..
  const resultTwo = await promiseTwo(); // 위 코드의 프로미스가 반환될 때까지 대기...

  console.log(resultTwo); // 완료 되면 하단의 코드가 이어서 실행됨

  const parellOne = promise(); // 위 아래 타이머는 동시에 시작됨.
  const parelltwo = promiseTwo(); // 해당 프로미스 이행 값이 먼저 반환됨.(약 1초)

  console.log(await parellOne);
  console.log(await parelltwo); // 먼저 프로미스 객체가 반환되었지만 위 함수가 먼저 실행되어야 실행됨.
}

foo(); // 콘솔에 찍히는 값은 순서대로 1 2 3 "one" 3 "two" "one"
```

분명 비동기 Promise가 위에서 작동하지만
해당 코드를 읽다보면 마치 동기 흐름처럼 자연스럽게 코드가 이어지는 것을 확인할 수 있다.

## Error handling in async/await

오류 처리를 위해서 async/await은 `try...catch`을 사용할 수 있다.

```javascript
async function getMaster() {
  try {
    const user = await Promise.reject(new Error("Error!!"));
    const name = user.name;  // 아래 코드는 실행되지 않음
    if (name === "chan") {
      return name;
    }
  } catch (error) {
    console.log(error); // "Error!!"를 출력
  }
}
```

`try`문에서 어떤 곳에서든지 에러가 발생하면 제어 흐름이 `catch`블록으로 넘어간다.
이는 마찬가지로 동기식 코드에서 에러 핸들링을 하는 것고 유사하다는 점에서 또 장점을 발휘한다.