// 요즘 잘 사용되지 않는  class 컴포넌트이기 때문에 state 부분은 이런 것이 있다고만 알고 넘어가자.
// state: 리액트 컴포넌트의 변경 가능한 데이터. 변경되면 렌더링이 다시 되기 때문에 이에 관련된 값만 포함해야 함. 하나의 JS 객체
// - 직접 수정할 수 없고, setState() 함수를 이용해야 한다.
// Life cycle

import React from "react";

const styles = {
  wrapper: {
    margin: 8,
    padding: 8,
    display: "flex",
    flexDirection: "row",
    border: "1px solid grey",
    borderRadius: 16,
  },
  messageText: {
    color: "black",
    fontSize: 16,
  },
};

class Notification extends React.Component {
  constructor(props) {
    super(props);

    this.state = {};
  }

  componentDidMount() {
    console.log(`${this.props.id} componentDidMount() called.`);
  }

  componentDidUpdate() {
    console.log(`${this.props.id} componentDidUpdate() called.`);
  } 

  componentWillUnmount() {
    console.log(`${this.props.id} componentWillUnmount() called.`);
  }

  render() {
    return (
      <div style={styles.wrapper}>
        <span style={styles.messageText}>{this.props.message}</span>
      </div>
    );
  }
}

export default Notification;