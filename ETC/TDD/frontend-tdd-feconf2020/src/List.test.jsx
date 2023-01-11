// App.jsx에서 썼던 테스트 코드를 가져와서 List로 바꿔만 준다.
// 테스트 코드를 다 작성했으면 App.jsx를 복사해 List.jsx도 만든다.
import React from 'react';
import { fireEvent, render } from '@testing-library/react';
import List from './List';
import tasks from '../fixtures/tasks';

// * BDD: 행동 유형에 따라서 테스트
// with tasks
// renders tasks

// without tasks
// renders no task message

describe('List', () => {
  const handleClick = jest.fn();
  // 세 번 중복되는 render 중복 제거
  function renderList(tasks) {
    return render((
      <List
        tasks={tasks}
        onClick={handleClick}
      />
    ));
  }

  context('with tasks', () => {
    const tasks = [
      { id: 1, title: '점심 메뉴 고민하기' },
      { id: 2, title: '고양이 사진 보기' },
    ];    
    it('renders tasks', () => {
      // * container: 해당 컴포넌트의 최상위 DOM
      const { container } = renderList(tasks)

      expect(container).toHaveTextContent('점심 메뉴 고민하기')
      expect(container).toHaveTextContent('고양이 사진 보기')
      // * 두 개의 리스트 요소를 모두 작성했으면 최종적으로 App.jsx에 List를 사용할 수 있도록 import 해주러 가자.
    });
  });

  it('renders "완료" buttons to delete a task', () => {
    // * container: 해당 컴포넌트의 최상위 DOM
    const { getAllByText } = renderList(tasks)

    const buttons = getAllByText('완료')

    fireEvent.click(buttons[0])

    expect(handleClick).toBeCalledWith(1)
  });

  context('without tasks', () => {
    const tasks = []
    it('renders no task message', () => {
      const { container } = renderList(tasks)
      expect(container).toHaveTextContent('할 일이 없네!')
    })
  })
})
