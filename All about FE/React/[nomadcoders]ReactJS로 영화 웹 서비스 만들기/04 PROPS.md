# 04 PROPS

## 04-1 Props

### 컴포넌트 재활용을 위한 Props

```react
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>replit</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
  <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <script type="text/babel">
    const root = document.getElementById("root");

    function Btn({ buttonName }) {
      return (
        <button
          style={{
            backgroundColor: "teal",
            color: "white",
            padding: "10px 20px",
            border: 0,
            borderRadius: "10px",
            marginRight: "5px",
          }}
        >
          {buttonName}
        </button>
      );
    }

    const App = () => {
      return (
        <div>
          <Btn buttonName={"Save Changes"} />
          <Btn buttonName={"Confirm"} />
        </div>
      );
    };

    ReactDOM.render(<App />, root);
  </script>
</html>
```



## 04-2 Memo

### .memo()

부모 컴포넌트의 한 가지 prop이라도 변경되면 자식 컴포넌트는 전부 재렌더링 되는데, 이러한 불필요한 성능 저하를 막기 위해 memo를 사용한다.

```react
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>replit</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
  <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <script type="text/babel">
    const root = document.getElementById("root");
    
    function Btn({ buttonName, changeName }) {
      console.log(buttonName, "redered");
      return (
        <button
          onClick={changeName}
          style={{
            backgroundColor: "teal",
            color: "white",
            padding: "10px 20px",
            border: 0,
            borderRadius: "10px",
            marginRight: "5px",
          }}
        >
          {buttonName}
        </button>
      );
    }
    const MemorizedBtn = React.memo(Btn);
    const App = () => {
      const [name, setName] = React.useState("Save Changes");
      const changeName = () => setName("Revert Changes");
      return (
        <div>
          <MemorizedBtn buttonName={name} changeName={changeName} />
          <MemorizedBtn buttonName={"Confirm"} />
        </div>
      );
    };
    
    ReactDOM.render(<App />, root);
  </script>
</html>
```



## 4-2. Prop Types

### React는 내가 어떤 타입의 props를 보내주고 싶은지 모른다. 

```markdown
https://unpkg.com/prop-types@15.7.2/prop-types.js
그리고 propType이 적용 안되시는 분들은
https://unpkg.com/react@17.0.2/umd/react.production.min.js ->
https://unpkg.com/react@17.0.2/umd/react.development.js 로 변경해주세요.
```





### PropTypes 패키지

1. 리액트는 파라미터를 잘 못 넘겨도 확인할 수 없는 문제점이 존재한다.
2. 이런 문제를 줄이기 위해서 PropTypes라는 모듈의 도움을 받을 수 있다.
3. type과 다르게 입력 되었을 경우 warning을 뜨게 할수 있고, parameter 에 값을 넣지 않는 경우 경고 메시지를 띄울수 있다.

```react
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>replit</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
  <script src="https://unpkg.com/react@17.0.2/umd/react.development.js"></script>
  <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/prop-types@15.7.2/prop-types.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <script type="text/babel">
    function Btn({ buttonName, fontSize = 10 }) {
      return (
        <button
          style={{
            backgroundColor: "teal",
            color: "white",
            padding: "10px 20px",
            border: 0,
            borderRadius: "10px",
            marginRight: "5px",
            fontSize,
          }}
        >
          {buttonName}
        </button>
      );
    }
    Btn.propTypes = {
      buttonName: PropTypes.string.isRequired,
      fontSize: PropTypes.number,
    };
    const App = () => {
      return (
        <div>
          <Btn buttonName={"Save Changes"} fontSize={20} />
          <Btn buttonName={"Confirm"} />
        </div>
      );
    };

    const root = document.getElementById("root");
    ReactDOM.render(<App />, root);
  </script>
</html>
```



