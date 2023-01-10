import React from 'react';
import List from './List';

export default function App() {
  // 데이터도 여기로 가져와서 직접 전달해준다.
  const tasks = [
    { id: 1, title: '점심 메뉴 고민하기'},
    { id: 2, title: '고양이 사진 보기'},
  ]
  return (
    <div>
      <h1>To-do</h1>
      {/* '아무 일도 하기 싫다' 요소를 작성한다. */}
      {/* <ul>
        <li>아무 일도 하기 싫다</li>
      </ul> */}
      {/* 하지만 TDD의 원칙 중 하나인 관심사의 분리에 따라 list에 대한 관심은 list 컴포넌트로 분리하자. */}
      {/* List와 List.test 컴포넌트 두 개를 생성한다. */}
      <List tasks={tasks} />
    </div>
  );
}
