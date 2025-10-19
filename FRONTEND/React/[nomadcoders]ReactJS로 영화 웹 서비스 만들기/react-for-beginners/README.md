# React for Beginners

- 1 컴포넌트 당 1개의 .js 파일을 가질 수 있어서 모듈화가 가능하다.
- 컴포넌트별 스타일은 .module.css 파일을 생성 + import 하여 사용
=> 여기서 스타일은 className이나 id로 import한 스타일 객체의
property를 전달하여 적용된다는 것! 이는 기존의 "어떤 class나 id에 적용할 스타일"이 아닌 "특정 jsx element에 적용할 스타일"로 생각할 수 있다~ react 컴파일 과정 중 random class나 id가 생성되기 때문에 .css 파일의 class, id 이름을 굳이 외울 필요없다
- create-react-app을 사용하면 React 앱 스캐폴딩을 생성해준다

const [counter, setValue] = useState(0);
-> 리액트 앱으로 하는 중이라 앞에 React 안붙여도됨

state를 변경할 때 ‘모든’ code 들을 항상 다시 실행됨
첫 번째 render에만 코드가 실행되고 다른 state변화에는 실행되지 않도록 만들자
예) API를 통해 데이터를 가져올 때 컴포넌트 렌더에서 API를 부르고
이후 상태가 변화할 때 그 API에서 데이터를 다시 가져오지 않게 만들 수 있다.

useEffect
- 두 개의 argument를 가지는 함수
- 첫 번째 argument는 우리가 딱 한번만 실행하고 싶은 코드
- 두 번째는 [] 배열을 넣어줌
-> useEffect가 컴포넌트의 첫 번째 렌더 시점에 iRunOnlyOnce 함수 호출
그리고 상태를 변화시키면 iRunOnlyOnce는 호출되지 않음
즉, 한번만 렌더링 됨
단순화 하여 useEffect(() => {
console.log("CALL THE API")
},[]); 써도 됨

useEffect 글자를 타이핑할 때마다 API를 새로 호출하지 않고 한번만 호출해준다.

search keyword에 변화가 있을 때 만! marvel영화를 검색하고 싶을 때
즉, 특정한 코드만 변화했을 때 원하는 코드들을 실행할 수 있는 방법
-> useEffect(() => {
console.log("SEARCH FOR", keyword);
}, []);
이렇게 실행하면 1번만 됨
그리고 []자리에 keyword 써줌
-> keyword가 변화할 때 코드를 실행할 거라고 react.js에게 알려주는 것.
이것이 바로 빈 array를 써주었을 때 코드가 단 한번만 실행되는 이유임
react가 지켜볼 게 아무것도 없으니 처음 한번만 실행되는 것

useEffect(() => {
console.log("I run when 'keyword & counter' changes.")
}, [keyword, counter]);
-> 2개도 가능

• 리액트를 사용하는 이유: 최소 단위의 렌더링을 위해
• useState(): 변수, 변수를 제어하는 함수로 구성되며 변하는 값을 제어, 해당 부분의 리렌더링을 위함
• props: 태그의 속성 값을 함수의 아규먼트 처럼 컴포넌트에 값을 전달해준다.
• useEffect(): 코드의 실행 시점을 관리할 수 있는 선택권을 얻는 방어막 같은 존재, 디펜던시가 없을 경우 최초 1회 실행, 있을 경우 해당 값이 변할 경우 실행한다. 이 때 디펜던시는 여러개 입력이 가능하다.

Hello 컴포넌트를 hide할 때는 컴포넌트가 스크린에서 지워지고
show를 누르면 컴포넌트가 다시 생성되므로
useEffect도 다시 실행됨을 알 수 있다.
-> 정해준 useEffect가 컴포넌트가 생성될 때 콘솔 로그를 하라는 것이기 때문
function Hello() {
useEffect(() => {
console.log("Hi");
}, []);

컴포넌트가 destroy될 때도 코드를 실행할 수 있다
-> return으로 함수를 만들어주면 된다.
useEffect는 함수를 받고, 이 함수는 dependency가 변화할 때 호출됨
현재는 dependency가 비어있으니 컴포넌트가 처음 생성될 때 함수가 호출된 후 다시
호출 되지 않음
그래서 컴포넌트가 파괴될 때도 함수를 실행하고 싶으면
useEffect 함수가 새로운 함수를 return해야 함
-> 왜냐면 deps가 비어있으면 자동으로 컴포넌트가 파괴될 때 cleanup함수가 실행되는데 그 과정이 리렌더링으로 useEffect함수가 실행되고 클린업하면서 이전에 있던 이펙트인 console.log(“created :) )가 삭제되고 새로운 이펙트 함수인 return함수가 실행되기 때문이다.
리렌더링 -> 이전 이펙트 클린업 -> 이펙트 실행