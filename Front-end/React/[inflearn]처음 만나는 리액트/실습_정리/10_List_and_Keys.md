# List and Keys

## List

목록, JavaScript의 배열 자료구조를 사용한다.

```react
const numbers = [1, 2, 3, 4, 5]
```



## Key

각자 객체나 아이템을 구분할 수 있는 고유한 값. map() 함수 내에서 필수적인 요소이다.



## 여러 개의 Component 랜더링하기

`map()`함수를 활용: 배열에 들어있는 변수들에 각각 처리를 한 뒤 return한다.

```react
const doubled = numbers.map((number) => number * 2);
```

```react
function NumberList(props) {
    const { number } = props;
    
    const listItems = numbers.map((number) =>
		<li>{number}</li>
	);
    
    return (
        <ul>{listItems}</ul>
    );
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
    <NumberList numbers={numbers} />
    document.getElementById('root')
);
```