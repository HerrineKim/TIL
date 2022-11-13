import React, { useState, useEffect } from "react";
import useCounter from "./useCounter";

const MAX_CAPACITY = 10;

function Accommodate(props) {
  const [isFull, setIsFull] = useState(false);
  const [count, increaseCount, decreaseCount] = useCounter(0);

  // React hooks: React에서 기존에 사용하던 Class를 이용한 코드를 작성할 필요 없이 여러 기능 사용할 수 있는 라이브러리
  // 함수형 컴포넌트에서만 사용
  // 의존성 배열이 없어 컴포넌트가 마운트 된 직후 호출되고, 컴포넌트 업데이트 될 때마다 호출
  useEffect(() => {
  // useEffect: 렌더링 이후 실행할 코드. 의존성 가질 수 있다.
    console.log("=====================");
    console.log("useEffect() is called");
    console.log(`isFull: ${isFull}`);
  });

  // 컴포넌트가 마운트 된 직후 호출되고, count 값이 바뀔 때마다 호출
  useEffect(() => {
    setIsFull(count >= MAX_CAPACITY);
    console.log(`Current count value: ${count}`);
  }, [count]);

  return (
    <div style={{ padding: 16 }}>
      <p>{`총 ${count}명 수용했습니다.`}</p>
      <button onClick={increaseCount} disabled={isFull}>
        입장
      </button>
      <button onClick={decreaseCount}>퇴장</button>
    </div>
  );
}

export default Accommodate;