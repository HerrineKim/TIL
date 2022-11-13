# Conditional Rendering

_어떤 조건에 따라 렌더링 여부가 달라지는 것._

예)

```react
function Greeting(props) {
    const isLoggedIn = props.isLoggedIn;
    
    if (isLoggedIn) {
        return <UserGreeting />;
    }
    return <GuestGreeting />;
}
```



## Inline Conditions

_조건문을 코드 안에 집어 넣는 것_



### 1. Inline If

_단축평가를 사용_

```react
function Mailbox(props) {
    const unreadMessages = props.unreadMessages;
    
    return (
        <div>
            <h1>안녕하세요!</h1>
            {unreadMessages.length > 0 &&
                <h2>현재 {unreadMessages.length}개의 읽지 않은 메시지가 있습니다.</h2>
            }
        </div>
    );
}
```



### 2. Inline If-else

? 연산자를 사용

`condition ? true : false`

```react
function UserStatus(props) {
    return (
        <div>
            이 사용자는 현재 <b>{props.isLoggedIN ? '로그인' : '로그인하지 않은'}</b> 상태입니다.
        </div>
    )
}
```



## Component 렌더링 막기

null을 리턴하면 렌더링되지 않음

```react
function WarningBanner(props) {
    if (!props.warning) {
        return null;
    }
    
    return (
        <div>경고!</div>
    );
}
```

