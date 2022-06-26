# Event

Event: 사건

#### DOM의 Event

```html
<button onClick="activate()">
    Activate
</button>
```

#### React의 Event

- Camel Case

```react
<button onClick="{activate}">
    Activate
</button>
```



Event Handler: 이벤트가 발생하면, 이벤트를 처리



## 1. 함수형 컴포넌트에서 event handler

```react
function Toggle(props) {
    const [isToggleOn, setIsToggleOn] = useState(true);
    
    // 방법 1. 함수 안에 함수로 정의
    function handleClick() {
        setIsToggleOn((isToggleOn) => !isToggleOn);
    }
    
    // 방법 2. arrow function을 사용하여 정의
    const handleClick = () => {
        setIsToggleOn((isToggleOn) => !isToggleOn);
    }
    
    return (
    	<button onClick={handleClick}>
        	{isToggleOn ? "켜짐" : "꺼짐"}
        </button>
    )
}
```