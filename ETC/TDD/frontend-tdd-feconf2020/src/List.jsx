// List 컴포넌트를 만들고 테스트를 하면 통과가 잘 되는 것을 볼 수 있다.
// 데이터를 외부로부터 받아서 리스트를 그리는 형태로 고쳐 보자.
// tasks 객체를 props로 받아와서 map 함수를 사용해 요소를 그려준다.
import React from 'react';

export default function List({ tasks }) {
  return (
      <ul>
        {
          tasks.map((task) => (
            <li key={task.id}>{task.title}</li>
          ))
        }
      </ul>
  );
}
