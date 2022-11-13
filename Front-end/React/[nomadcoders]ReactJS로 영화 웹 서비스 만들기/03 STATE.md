# 03 STATE

## 3.1 setState part One

- 데이터가 바뀔 때마 다시 렌더링을 하는 것보다, React 상의 하나의 공간에 데이터를 담아두고 필요할 때마다 가져다 쓰는 것이 효율적



## 3.2 setState part Two

```react
const root = document.getElementById("root");
function App() {
    const [counter, setCounter] = React.useState(0);
    // state를 바뀌고, 컴포넌트를 재랜더링 해주는 setCounter
    const onClick = () => {
        setCounter(counter + 1);
    };
    return (
        <div>
            <h3>Total clicks: {counter}</h3>
            <button onClick={onClick}>Click me</button>
        </div>
    );
};
```



## 3.3 Recap



## 3.4 State Functions

```react
const root = document.getElementById("root");
function App() {
    const [counter, setCounter] = React.useState(0);
    // state를 바뀌고, 컴포넌트를 재랜더링 해주는 setCounter
    const onClick = () => {
        setCounter(counter + 1);
    };
    return (
        <div>
            <h3>Total clicks: {counter}</h3>
            <button onClick={onClick}>Click me</button>
        </div>
    );
};
```

```react
const root = document.getElementById("root");
function App() {
    const [counter, setCounter] = React.useState(0);
    // state를 바뀌고, 컴포넌트를 재랜더링 해주는 setCounter
    const onClick = () => {
        setCounter((current) => current + 1);
    };
    return (
        <div>
            <h3>Total clicks: {counter}</h3>
            <button onClick={onClick}>Click me</button>
        </div>
    );
};
```



## 3.5 Inputs and State

```react
function App() {
    return (
        <div>
        	<h1>Super Converter</h1>
            <label>Minutes</label>
        	<input id="minutes" placeholder="Minutes" type="number" />
            <label>Hours</label>
            <input id="hours" placeholder="Hours" type="number" />
        </div>
    );
}
const root = document.getElementById("root");
ReactDOM.render(<App />, root);
```



### JSX만의 문법: for과 같은 표현은 쓸 수 없다.

- JSX를 쓰고 있어 htmlFor로 바꾸어야 한다. 즉, 별도의 문법이 존재한다.



### state 값을 업데이트 받아 표시하기

```react
function App() {
    const [minutes, setMinutes] = React.useState();
    const onChange = (event) => {
        setMinutes(event.target.value);
    };
    return(
        <div>
            <h1 className="hi">Super Converter</h1>
            <label htmlFor="minutes">Minutes</label>
            <input
                value={minutes}
                id="minutes"
                placeholder="Minutes"
                type="number"
                onCahnge={onChange}
            />
            <h4>You want to convert {minutes}</h4>
            <label htmlFor="hours">Hours</label>
            <input id="hours" placeholders="Hours" type="number" />
        </div>
    );
}
```



## 3.6 State Practice part One

### 복습

- value 쓰는 이유: 외부에서도 value값 수정해주기 위해



### 분 - 시 연동과 reset

```react
function App() {
    const [minutes, setMinutes] = React.useState();
    const onChange = (event) => {
        setMinutes(event.target.value);
    };
    const reset = () => setMinutes(0)
    return(
        <div>
            <h1 className="hi">Super Converter</h1>
            <label htmlFor="minutes">Minutes</label>
            <input
                value={minutes}
                id="minutes"
                placeholder="Minutes"
                type="number"
                onCahnge={onChange}
            />
            <div>
                <label htmlFor="hours">Hours</label>
                <input
                    value={Math.round(minutes / 60)}
                    id="hours"
                    placeholders="Hours"
                    type="number" />
            </div>
            <button onClick={reset}>Reset</button>
        </div>
    );
}
```





## 3.7 State Practicepart Two

### 시, 분 입력 전환

```react
function App() {
    const [minutes, setMinutes] = React.useState(0);
    const [flipped, setFlipped] = React.useState(false);
    const onChange = (event) => {
        setMinutes(event.target.value);
    };
    const reset = () => setMinutes(0)
    const onFlip = () => {
        reset();
        setFlipped((cuurent) => !current);
    }
    return(
        <div>
            <h1 className="hi">Super Converter</h1>
            <label htmlFor="minutes">Minutes</label>
            <input
                value={flipped ? minutes * 60: minutes}
                id="minutes"
                placeholder="Minutes"
                type="number"
                onCahnge={onChange}
                disabled={flipped === true}
            />
            <div>
                <label htmlFor="hours">Hours</label>
                <input
                    value={flipped ? minutes : Math.round(minutes / 60)}
                    id="hours"
                    placeholders="Hours"
                    type="number"
                    disabled={flipped === false}
                 />
            </div>
            <button onClick={reset}>Reset</button>
            <button onClick={onFlip}>Flip</button>
        </div>
    );
}
```



## 3.8 Recap



```react
function App() {
    const [minutes, setMinutes] = React.useState(0);
    const [flipped, setFlipped] = React.useState(false);
    const onChange = (event) => {
        setMinutes(event.target.value);
    };
    const reset = () => setMinutes(0)
    const onFlip = () => {
        reset();
        setFlipped((cuurent) => !current);
    }
    return(
        <div>
            <h1>Super Converter</h1>
            <h1 className="hi">Super Converter</h1>
            <label htmlFor="minutes">Minutes</label>
            <input
                value={flipped ? minutes * 60: minutes}
                id="minutes"
                placeholder="Minutes"
                type="number"
                onCahnge={onChange}
                disabled={flipped}
            />
            <div>
                <label htmlFor="hours">Hours</label>
                <input
                    value={flipped ? minutes : Math.round(minutes / 60)}
                    id="hours"
                    placeholders="Hours"
                    type="number"
                    disabled={!flipped}
                    onChange={onChange}
                 />
            </div>
            <button onClick={reset}>Reset</button>
            <button onClick={onFlip}{Flipped ? "Turn back" : "Flip" }</button>
        </div>
    );
}
```



## 3.9 Final Practice and Recap

### 이전 코드를 변환하여 속도 변환기 만들기

```react
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>React Basic</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
  <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <script type="text/babel">
    function MinutesToHours() {
      const [amount, setAmount] = React.useState(0);
      const [inverted, setInverted] = React.useState(false);
      const onChange = (event) => {
        setAmount(() => event.target.value);
      };
      const onInverted = () => {
        setInverted((current) => !current);
        return setAmount(() => 0);
      };
      return (
        <div>
          <h3>Minutes to Hours</h3>
          <div>
            <label htmlFor="minutes">Minutes</label>
            <input
              value={inverted ? amount * 60 : amount}
              id="minutes"
              placeholder="Minutes"
              type="number"
              onChange={onChange}
              disabled={inverted}
            />
          </div>
          <div>
            <label htmlFor="Hours">Hours</label>
            <input
              value={inverted ? amount : Math.round(amount / 60)}
              id="Hours"
              placeholder="Hours"
              type="number"
              disabled={!inverted}
              onChange={onChange}
            />
          </div>
          <button onClick={() => setAmount(() => 0)}>Reset</button>
          <button onClick={onInverted}>
            {inverted ? "Turn back" : "Invert"}
          </button>
        </div>
      );
    }
    function KmToMiles() {
      const [amount, setAmount] = React.useState(0);
      const [invert, setInvert] = React.useState(false);
      const kmChange = (event) => {
        setAmount(() => event.target.value);
      };
      return (
        <div>
          <h3>KM to Miles</h3>
          <div>
            <label htmlFor="km">Kilometers</label>
            <input
              onChange={kmChange}
              disabled={invert}
              value={invert ? parseFloat(amount * 1.60934).toFixed(4) : amount}
              id="km"
              placeholder="Kilometers"
              type="number"
            />
          </div>
          <div>
            <label htmlFor="miles">Miles</label>
            <input
              onChange={kmChange}
              value={invert ? amount : parseFloat(amount * 0.621371).toFixed(4)}
              disabled={!invert}
              id="miles"
              placeholder="Miles"
              type="number"
            />
          </div>
          <button onClick={() => setAmount(() => 0)}>Reset</button>
          <button
            onClick={() => {
              setInvert((current) => !current);
              return setAmount(() => 0);
            }}
          >
            {invert ? "Invert" : "Turn back"}
          </button>
        </div>
      );
    }
    function App() {
      const [index, setIndex] = React.useState("1");
      const onSelect = (event) => {
        return setIndex(() => event.target.value);
      };
      return (
        <div>
          <h1>Super Converter</h1>
          <select onChange={onSelect}>
            <option value="-1">Select Unit</option>
            <option value="0">Minutes & Hours</option>
            <option value="1">Km & Miles</option>
          </select>
          <hr />
          {index === "0" ? (
            <MinutesToHours />
          ) : index === "1" ? (
            <KmToMiles />
          ) : null}
        </div>
      );
    }
    const root = document.getElementById("root");
    ReactDOM.render(<App />, root);
  </script>
</html>
```

