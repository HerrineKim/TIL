import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import Item from './Item';

test('Item', () => {
  // 샘플 데이터
  const task = {
    id: 1,
    title: '뭐라도 하기',
  };
  // 가짜 함수를 만들어주는 jest.fn()
  const handleClick = jest.fn();
  // container(최상위 DOM)과 getByText(특정 문자를 가진 엘리먼트가 있는지 체크 해주는 쿼리)
  const { container, getByText } = render((
    <Item
      task={task}
      onClickDelete={handleClick}
    />
  ));

  expect(container).toHaveTextContent('뭐라도 하기');
  expect(container).toHaveTextContent('완료');
  // toBeCalled(): 함수가 호출되는지 체크. 앞에 not을 붙여 호출되지 않아야 통과
  expect(handleClick).not.toBeCalled();
  // 클릭 이벤트 발생!
  fireEvent.click(getByText('완료'));
  // toBeCalledWith(): 설정한 인자(숫자일 경우 횟수)로 함수가 실행되는지 확인
  // 1번 실행되었는지 확인하니까 통과!
  expect(handleClick).toBeCalledWith(1);
});
