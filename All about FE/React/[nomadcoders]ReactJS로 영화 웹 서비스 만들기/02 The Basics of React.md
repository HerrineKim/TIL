# 02 The Basics of React

- React는 UI를 interactive하게 만들어준다

- vanillaJS로 작업하는 것은 처음에는 괜찮지만, 이벤트가 많아질수록 너무 복잡하게 된다.



## 02-1 React와 vanillaJS의 다른 점

- vanillaJS는 HTML 요소를 먼저 생성하고 그것을 JS로 조작했다면, React는 자신이 HTML을 생성한다.
  - JS로 element를 생성하고, React는 그것을 HTML로 번역한다. 



## 02-2 ReactJS의 파워

- event listener를 추가하는 대신 함수를 사용하여 props 안에서 event를 추가할 수 있다.



## 02-3 JSX

- JSX는 createElement를 더 편리하게 대체해준다. html 문법 안에서 모든 이벤트를 작성할 수 있다.
- Babel은 이 코드를 브라우저가 이해할 수 있도록 JS코드로 변환해준다.